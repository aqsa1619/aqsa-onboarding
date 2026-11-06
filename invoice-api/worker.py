import json
import time

from db import Base, SessionLocal, engine
from db_models import InvoiceRow, JobRow
from report import build_report

Base.metadata.create_all(engine)   # make sure the tables exist


def process_one_job() -> bool:
    """Take one queued job and finish it. Return False if none were waiting."""
    db = SessionLocal()
    try:
        # 1. Find the oldest job that is still waiting
        job = (
            db.query(JobRow)
            .filter(JobRow.status == "queued")
            .order_by(JobRow.id)
            .first()
        )
        if job is None:
            return False

        # 2. Mark it as running, so nobody else picks it up
        job.status = "running"
        db.commit()
        print(f"Job {job.id}: running")

        try:
            time.sleep(5)  # pretend the report is slow (lets you show "running")

            # 3. Build the report using your existing report.py
            invoices = db.query(InvoiceRow).all()
            report = build_report(invoices)

            # 4. Save the result and mark it done
            job.result = json.dumps(report)
            job.status = "done"
            print(f"Job {job.id}: done")
        except Exception as error:
            job.status = "failed"
            job.result = json.dumps({"error": str(error)})
            print(f"Job {job.id}: failed ({error})")

        db.commit()
        return True
    finally:
        db.close()


if __name__ == "__main__":
    print("Worker started. Waiting for jobs... (Ctrl+C to stop)")
    while True:
        found_job = process_one_job()
        if not found_job:
            time.sleep(2)   # nothing waiting, rest a moment and check again