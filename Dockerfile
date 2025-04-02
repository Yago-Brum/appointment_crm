# Usar uma imagem base com Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do aplicativo
EXPOSE 8000

# Comando para rodar o Django com o Gunicorn
CMD ["gunicorn", "appointment_crm.wsgi:application", "--bind", "0.0.0.0:8000"]
