# API

APIs best practices

## Representational State Transfer

1. Client-Server
2. Stateless
3. Cache
4. Layered System
5. Code On Demand

## API Calls

- `GET`/api/v1/products/123/items/active > **READ**
- `POST`/api/v1/products/123/items > **CREATE**
- `PUT`/api/v1/products/123/items/1 > **UPDATE**
- `DELETE`/api/v1/products/123/items/1 > **DELETE**

### API Responses

- `JSON`
- `XML`
- `YAML`

### HTTP Status Codes

- `1xx` Informational
- `2xx` Success
- `3xx` Redirection
- `4xx` Client Error
- `5xx` Server Error

### API Versioning

- `https://example-api.com/api/v1/products/123/items/`
- `https://example-api.com/api/products/123/items/?version=1`
