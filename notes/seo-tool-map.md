# SEO Tool Map

## Backend files (one line each)
- app/main.py: HTTP API (auth, options, estimate, create_run, run/stage reads, rerun, resume, admin)
- app/worker.py: polls the jobs table, claims a queued job, calls execute_run
- app/models.py: tables User, Run, StageResult, Job, ProviderCall, CacheEntry
- app/pipeline/runner.py: enqueue, invalidate_from, execute_run (resume + saving results)
- app/pipeline/stages.py: STAGES dict and the stage 1-3 functions
- app/providers/: provider interface + cached_call, DataForSEO adapter, mock adapter
- app/llm.py: LLMGateway (Anthropic/Gemini), records cost
- app/costs.py: CostTracker, estimate_run, check_caps, CapExceeded
- app/cli.py: create-admin, check-dataforseo
- config/app.yaml: thresholds, caps, prices, locations, models

## Page -> endpoint
- New run (frontend/app/runs/new/page.tsx):
  GET /api/options, POST /api/runs/estimate, POST /api/runs
- Run page (frontend/app/runs/[id]/page.tsx):
  GET /api/runs/{id}, GET /api/runs/{id}/stages/1|2|3,
  POST /api/runs/{id}/rerun, POST /api/runs/{id}/resume
- Runs list, Admin: not read yet

## Where a stage result is saved
Table stage_results (models.py: StageResult), written by runner.py execute_run
after each stage: output (JSON), status, cost_usd. One row per (run_id, stage).

## One run in the data flow
form -> POST /api/runs -> Run + Job rows -> worker claim_job -> execute_run
-> StageResult rows -> run page polls and reads them