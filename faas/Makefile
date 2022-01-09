include ../.env

build_faas:
	env GITHUB_USERNAME=${GITHUB_USERNAME} faas-cli publish -f webtorrent.yml --platforms ${OPENFAAS_ARCH}

deploy_faas:
	env GITHUB_USERNAME=${GITHUB_USERNAME} faas-cli deploy --gateway ${OPENFAAS_GATEWAY} -f webtorrent.yml

login_faas:
	faas-cli login --gateway ${OPENFAAS_GATEWAY} --password ${OPENFAAS_PASS}