#!/bin/bash

source .env

# create database
psql -U postgres <<EOF
CREATE DATABASE maindb;

\c maindb

CREATE SCHEMA schema1;

CREATE ROLE ytber WITH LOGIN PASSWORD '$ROLE_PASSWORD';

GRANT ALL PRIVILEGES ON SCHEMA schema1 TO ytber;
EOF

exit $?


# end of script