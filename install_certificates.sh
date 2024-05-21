mkcert -install
if [ ! -d "certs" ]; then
    mkdir certs
fi
mkcert -cert-file certs/local-cert.pem -key-file certs/local-key.pem "maestro.localhost" "172.30.0.1"
