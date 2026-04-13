import flet as ft
import random

def main(page: ft.Page):
    imagem_correta = random.choice(["Mario", "Luigi"])
    
    mensagem = ft.Text(
        f"Clique no {imagem_correta}",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    def jogar(e):
        # CORREÇÃO 1: Usando 'data' para identificar qual botão foi clicado
        imagem_selecionada = e.control.data

        # mostra a imagem ao clicar
        e.control.image.opacity = 1.0

        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            mensagem.value = f"Ops! Não é o {imagem_correta}."

        container_mario.on_click = None
        container_luigi.on_click = None

        btn_jogar_novamente.visible = True
        page.update()
    
    def jogar_novamente(e):
        nonlocal imagem_correta

        imagem_correta = random.choice(["Mario", "Luigi"])
        mensagem.value = f"Clique no {imagem_correta}"

        btn_jogar_novamente.visible = False

        # esconde imagens novamente
        container_mario.image.opacity = 0.0
        container_mario.bgcolor = ft.Colors.GREY_200
        container_mario.on_click = jogar

        container_luigi.image.opacity = 0.0
        container_luigi.bgcolor = ft.Colors.GREY_200
        container_luigi.on_click = jogar

        # embaralha posições
        random.shuffle(linha_personagens.controls)

        page.update()

    container_mario = ft.Container(
        data="Mario",  # <-- Adicionado para identificar o container
        content=ft.Text(""),
        image=ft.DecorationImage(
            src="images/mario.png",
            fit=ft.BoxFit.COVER,
            opacity=0.0  # começa escondido
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    container_luigi = ft.Container(
        data="Luigi",  # <-- Adicionado para identificar o container
        content=ft.Text(""),
        image=ft.DecorationImage(
            src="images/luigi.png",
            fit=ft.BoxFit.COVER,
            opacity=0.0  # começa escondido
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    linha_personagens = ft.Row(
        [container_mario, container_luigi],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # CORREÇÃO 2: Alterado de ft.Button para ft.ElevatedButton
    btn_jogar_novamente = ft.ElevatedButton(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text("Selecione a imagem certa", size=24, weight="bold"),
                mensagem,
                linha_personagens,
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(main)