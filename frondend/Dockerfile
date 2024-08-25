# Используем базовый образ Node.js
FROM node:18

# Создаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY . .

# Собираем проект
RUN npm run build

# Указываем команду для запуска приложения
CMD ["npm", "start"]

# Открываем порт
EXPOSE 3000
