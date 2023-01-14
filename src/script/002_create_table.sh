#!/bin/bash

source .env

psql -U nohira <<EOF
\c maindb

-- SET search_path = schema1;

DROP TABLE IF EXISTS schema1.m_manage;
CREATE TABLE schema1.m_manage (
  uid			SERIAL		PRIMARY KEY,
  name			VARCHAR(30)	NOT NULL,
  created_at	TIMESTAMP	DEFAULT CURRENT_TIMESTAMP,
  modified_at	TIMESTAMP	DEFAULT CURRENT_TIMESTAMP
);

GRANT ALL PRIVILEGES ON schema1.m_manage TO ytber;

INSERT INTO schema1.m_manage( name ) VALUES ( 'nohira01' );
EOF

exit $?


# end of script