# Odoo MRP ↔ BSALE Integration

## Descripción
Integración bidireccional entre Odoo 19 (MRP) y BSALE desarrollada con FastAPI.
Permite sincronizar productos, stock y datos operativos utilizando APIs REST
y una base de datos MySQL como capa intermedia.

## Stack tecnológico
- Odoo 19 (MRP)
- BSALE API
- FastAPI
- MySQL

## Arquitectura
La integración utiliza MySQL como middleware para desacoplar Odoo y BSALE,
permitiendo sincronización bidireccional y control de estados.

## Público objetivo
Empresas que utilizan Odoo y BSALE y requieren sincronización automática
de datos operativos.