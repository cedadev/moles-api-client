# Updating client
1. copy schema.yml into this repo
2. python -m venv venv
3. activate venv
4. pip install openapi-python-client
5. openapi-python-client generate --path schema.yml --overwrite  --custom-template-path=templates 

# Using api client
1. python -m venv venv
2. activate venv
3. pip install ./moles-api-v-3-client   

# Scripts
Scripts directory contains fwe of the scripts from ingest machines recreated to use API approach.
Most of them require endpoint and access token as environmental vars e.g.
`export API_URL="http://localhost:8000/"`
`export API_TOKEN="exampleaccesstoken452708945279"`