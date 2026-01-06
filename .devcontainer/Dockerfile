FROM python:3.13.2-slim

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Dependências do sistema (matplotlib/seaborn precisam disso)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libgl1 \
    git \
    && rm -rf /var/lib/apt/lists/*


# Diretório de trabalho
WORKDIR /workspace

# Copia requirements primeiro (cache do Docker)
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# VSCode Dev Container gerenciara o bash
CMD ["sleep", "infinity"]