### Установка и запуск

1. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Запустите приложение**:
   ```bash
   python app.py
   ```

3. **Откройте документацию**:
   - Перейдите по адресу [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs).

---

### Пример использования

- **Получить токен**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "Jonh", "password": "123456"}' \
  http://127.0.0.1:5000/auth/login
  ```
  
- **Добавить транзакцию**:
  ```bash
  curl -X POST -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"amount": 1500}' \
  http://127.0.0.1:5000/users/transactions
  ```