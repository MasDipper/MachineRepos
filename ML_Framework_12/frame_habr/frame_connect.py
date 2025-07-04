import streamlit as st
import requests
import os

# Обнуление статусов прокси для корректного для корректного подключения
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPs_PROXY'] = ''

st.title('Предсказание кластера')
# Поле ввода
input_text = st.text_area('Введите текст статьи', height=200)

if st.button('Предсказать'):
    if input_text == '':
        st.write(f'Пустое поле! Введите текст')
    else:
        data = {
            'text': input_text
        }

        url = 'http://127.0.0.1:8000/predict'
        response = requests.post(url, json=data)
        result = response.json()
        clust = result.get('cluster')

        # Вывод предсказанного кластера
        st.markdown(f'''
            ### Результат:
        ''')
        st.write(f'Кластер: {clust[0]}')
        st.write(f'{clust[1]}')
