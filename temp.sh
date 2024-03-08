# Get DNS Records
curl --request GET --url https://api.cloudflare.com/client/v4/zones/2afbbfdaacb3914d9466920f316ac9f2/dns_records \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer OOWsqUXqpr3_uiDYwnGEMaJXLtRLZK0aTui0eSgg' \
    --data '{
    "content": "99.53.207.238",
    "name": "neilclack.com",
    "proxied": false,
    "type": "A",
    "comment": "Domain verification record",
    "tags": [""],
    "ttl": 3600
  }' | jq


# Update DNS Record
curl --request PATCH \
  --url https://api.cloudflare.com/client/v4/zones/2afbbfdaacb3914d9466920f316ac9f2/dns_records/0f101e476e17c76002b7670e63614ef6 \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer OOWsqUXqpr3_uiDYwnGEMaJXLtRLZK0aTui0eSgg' \
  --data '{
  "content": "99.53.207.238",
  "name": "neilclack.com",
  "proxied": true,
  "type": "A",
  "comment": "Domain verification record",
  "ttl": 120
}'