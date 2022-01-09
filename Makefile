include .env

build_faas:
	faas-cli publish -f faas/webtorrent.yml --platforms ${OPENFAAS_ARCH}

deploy_faas:
	faas-cli deploy --gateway ${OPENFAAS_GATEWAY} -f faas/webtorrent.yml

login_faas:
	faas-cli login --gateway ${OPENFAAS_GATEWAY} --password ${OPENFAAS_PASS}