# Price Monitor RPA - Nissei

Bot de Rocketbot que extrae productos de Nissei, genera un Excel y lo envía por correo.

## Funcionalidades

- Extracción de productos desde nissei.com
- Formateo de datos con Python
- Generación de reporte Excel
- Envío automático por email

## Requisitos

- Rocketbot Studio
- Python 3.x
- Módulos: pandas, openpyxl

## Configuración

1. Configurar servidor SMTP en Rocketbot
2. Crear contraseña de aplicación en Gmail
3. Configurar variable `lista_productos`

## Uso

1. Ejecutar el flujo `Price_Monitor_RPA`
2. El bot extraerá los productos automáticamente
3. Se generará un Excel en la carpeta exports/
4. Se enviará por correo al destinatario configurado
