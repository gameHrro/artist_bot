import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from data import art_idea, colors
from schemes import AddNewIdea
from fastapi import FastAPI
import random

app = FastAPI(title='ArtistBot')

@app.get('/get_idea/', tags=['💡 Идеи для рисунков'], summary='получаем все идеи для рисунка')
async def get_idea():
    return art_idea

@app.post('/add_idea/', tags=['💡 Идеи для рисунков'], summary='добавляем новую идею для рисунка')
async def add_idea(idea: AddNewIdea):
    art_idea.append(idea)

    return {'Новая идея': idea}

@app.get('/generate_idea/', tags=['💡 Идеи для рисунков'], summary='генерируем идею для рисунка')
async def generate_idea():
    idea = random.choice(art_idea)
    return {f'🎲 Ваша идея: {idea}'}

@app.get('/challenges/', tags=['🎯 Челлендж'], summary='генерируем челлендж')
async def challenges():
    colors_numbers = random.randint(1, 3)

    if colors_numbers == 1:
        idea = random.choice(art_idea)

        color = random.choice(colors)

        return {f'🎲 Идея {idea}', f'🔢 Кол-во цветов 1', f'🎨 Цвет {color}'}

    elif colors_numbers == 2:
        idea2 = random.choice(art_idea)

        color1 = random.choice(colors)
        color2 = random.choice(colors)

        return {f'🎲 Идея {idea2}', f'🔢 Кол-во цветов 2', f'🎨 Цвета {color1}, {color2}'}

    elif colors_numbers == 3:
        idea3 = random.choice(art_idea)

        color1 = random.choice(colors)
        color2 = random.choice(colors)
        color3 = random.choice(colors)

        return {f'🎲 Идея {idea3}', f'🔢 Кол-во цветов 3', f'🎨 Цвета {color1}, {color2}, {color3}'}

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, port=5050, host='127.0.0.5')