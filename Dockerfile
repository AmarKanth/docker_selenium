FROM python:3.9.1

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libxkbcommon0 \
    libxss1 \
    xdg-utils \
    gnupg2 \
    libasound2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libvulkan1 \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]