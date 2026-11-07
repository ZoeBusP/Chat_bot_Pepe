import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

pepe= commands.Bot(command_prefix="$", intents=intents)

@pepe.event
async def on_ready(): 
    print("Pepe ya esta en discord")

@pepe.command()
async def hola(ctx):
    await ctx.send(f"Hola, {ctx.author.name}. Soy Pepe, el bot que te va a salvar de morirte contaminado por el daño de los humanos")

@pepe.command()
async def ideas(ctx):
    await ctx.send("Si quieres ayudarme a salvar el planeta, puedes hacer cosas como: \n1. Eco-bloques. \n2. Clasificación de residuos. \n3. Ahorrar energía y agua. \n4. Apoyar a organizaciones ambientales. \n5. Educar a otros sobre la importancia de cuidar el medio ambiente. \nSi te gustaría aprender mas sobre estas ideas, enviame el comando $ayuda junto con el número de la idea y te ayudaré a lograrlo!")

@pepe.command()
async def ayuda(ctx, idea: int):
    if idea == 1:
        await ctx.send("Los eco-bloques son residuos que colocamos adentro de botellas plásticas, pueden ser envoltorios de galleta, papitas y esas cosas que comemos mientras scrolleamos en tik tok. Cuando se llene tu botella, oficialmente tienes listo tu eco-bloque, llevalo a tu centro de acopio mas cercano o en español un centro de reciclaje.")
    elif idea == 2:
        await ctx.send("La clasificación de residuos es el proceso de separar los diferentes tipos de basura para que puedan ser reciclados o eliminados de manera adecuada. Puedes hacerlo en casa, en tu escuela o en tu comunidad. Asegúrate de seguir las normas locales de reciclaje y de no mezclar materiales que no se pueden reciclar.")
    elif idea == 3:
        await ctx.send("Ahorrar energía y agua es importante para reducir nuestro impacto ambiental. Puedes hacerlo apagando luces y aparatos electrónicos cuando no los uses, utilizando bombillas de bajo consumo, tomando duchas más cortas y reparando fugas de agua. Cada pequeño cambio cuenta.")
    elif idea == 4:
        await ctx.send("Apoyar a organizaciones ambientales es una excelente manera de contribuir a la protección del medio ambiente. Puedes hacerlo donando dinero, tiempo o recursos a organizaciones que trabajen en la conservación de la naturaleza, la lucha contra el cambio climático y la educación ambiental.")
    elif idea == 5:
        await ctx.send("Educar a otros sobre la importancia de cuidar el medio ambiente es fundamental para generar conciencia y promover cambios positivos. Puedes hacerlo compartiendo información en redes sociales, organizando charlas o talleres, y enseñando a amigos y familiares sobre prácticas sostenibles.")
    else:
        await ctx.send("Lo siento, no tengo información sobre esa idea específica. Pero no importa siempre puedes ayudar al planeta con pequeñas acciones por ejemplo intenta no usar pajillas plasticas, no tirar basura en la calle, no desperdiciar comida y muchas cosas mas. Si quieres aprender mas sobre estas ideas, enviame el comando $ideas y te ayudare a lograrlo!")

@pepe.command()
async def redes(ctx):
    await ctx.send("Si quieres ayudarme a salvar el planeta, puedes publicar en tus redes sociales la importancia de cuidar el medio ambiente osea vas a ganas puntos con tus papas por ecofriendly y puedes ayudar a que tus amigos y familiares se unan a la causa. Puedes enviamre el comando $hashtags y te puedo enviar un hastag aleatorio para incluir en tus posts!")

@pepe.command()
async def hashtags(ctx):
    hashtags = [
        "#CuidemosElPlaneta",
        "#EcoFriendly",
        "#Recicla",
        "#SalvemosElMedioAmbiente",
        "#Sostenibilidad",
        "#CambioClimático",
        "#EnergíaRenovable",
        "#Conservación",
        "#Naturaleza",
        "#PlanetaVerde"
    ]
    hashtag_aleatorio = random.choice(hashtags)
    await ctx.send(f"¡Aquí tienes un hashtag aleatorio para tus posts! {hashtag_aleatorio}")

@pepe.command()
async def reto(ctx):
    retos = [
        "Reto 1: Apaga las luces y aparatos electrónicos cuando no los uses durante una semana.",
        "Reto 2: Reduce el uso de plásticos de un solo uso durante un mes.",
        "Reto 3: Planta un árbol o cuida uno existente en tu comunidad.",
        "Reto 4: Participa en una limpieza de tu vecindario o playa.",
        "Reto 5: Aprende a compostar y comienza a compostar tus residuos orgánicos."
    ]
    reto_aleatorio = random.choice(retos)
    await ctx.send(f"¡Aquí tienes un reto para ayudar al planeta! {reto_aleatorio}")

@pepe.command()
async def tips(ctx):
    tips = [
        "Tip 1: Usa bolsas reutilizables en lugar de bolsas de plástico.",
        "Tip 2: Bebe agua del grifo en lugar de comprar agua embotellada.",
        "Tip 3: Recicla papel, cartón, vidrio y plástico según las normas locales.",
        "Tip 4: Reduce el consumo de carne y productos animales para disminuir tu huella de carbono.",
        "Tip 5: Utiliza transporte público, bicicleta o camina en lugar de conducir siempre que sea posible."
    ]
    tip_aleatorio = random.choice(tips)
    await ctx.send(f"¡Aquí tienes un tip para ayudar al planeta! {tip_aleatorio}")

@pepe.command()
async def impacto(ctx):
    await ctx.send("El impacto ambiental es la alteración del medio ambiente causada por las actividades humanas. Esto incluye la contaminación del aire, agua y suelo, la deforestación, la pérdida de biodiversidad y el cambio climático. Cada acción que tomamos puede tener un efecto positivo o negativo en el planeta, por lo que es importante ser conscientes de nuestras decisiones y tratar de reducir nuestro impacto ambiental.")

pepe.run("Token de Pepe")