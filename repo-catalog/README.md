# Repository catalog

`repositories.yaml` is the curated inventory for the organization. Treat generated values as suggestions until owners verify them.

Required fields:
- `name`: repository name;
- `full_name`: `org/repo`;
- `url`: canonical GitHub URL;
- `visibility`: public, private, or internal;
- `archived`: boolean;
- `lifecycle`: active, maintenance, archived, or unknown;
- `owner`: team or accountable group (use `unknown` until assigned);
- `tier`: critical, high, standard, or sandbox;
- `primary_stack`: best-effort language/framework label.

Add service dependencies and data classification only after owner confirmation. Do not put secrets, internal hostnames, or sensitive operational details in the catalog.
