import sys
import os
# Добавляем путь к папке Users
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

# Добавляем путь к папке App
sys.path.append(os.path.join(os.path.dirname(__file__), 'bonus'))

sys.path.append(os.path.join(os.path.dirname(__file__), 'data_base'))