# ingestion
> retrive the documents assuming given data requirements
[data given]

> form a ingestion pipeline with given settings and implement open knowledge format.


# Prompts Used During Development

Exact prompts given during development, in order. Trimmed to the
significant ones (not every message in the session).

## Review & planning

> read the project and focus on further what we are building.context of assignment.
> [assignment brief pasted]


## Search architecture

> give a solution for elastic search docker continous running problem. should i use bm25 instead of elastic search. also does bm25 uses the same chunks used by semantic search. lets talk only

> cant i do native elastic search installation which will not use docker at all

> how about elastic search cloud .how our data will be sent to elastic cloud for key based searches


## GraphRAG

> lets add graph too

## Evaluation (Milestone 4)

> add 20 more values in the golden set where 10 of them asks cross documents questions inducing graph rag use. and remaining 10 asks info about specific cases and their verdicts(court judgements).

## Cleanup & deployment

> would i have to ditch embedded chunks too?

> still same error should i redploy on render after the build?. also where to see api calls and logs to find issue

