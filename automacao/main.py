from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

options = webdriver.ChromeOptions()
#options.add_argument("--window-size=1920,1080")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
navegador.implicitly_wait(10) # espera 10 segundos para todo comando

user = os.getenv("USER")
password = os.getenv("PASSWORD")
orgao = os.getenv("ORGAO")
processo = os.getenv("PROCESSO")
assunto = "Criação de número de patrimônio"
conteudo_oficio = f"""
<body>
    <p class="Texto_Alinhado_Esquerda"><strong>Assunto:{assunto}</strong></p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha"><strong>Senhora Primeiro Tenente BM Chefe de Curso do CFS -
            Caparaó,</strong></p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">Solicito a Vossa Senhoria autorização para liberação das minhas
        atividades de curso,&nbsp;no período da manhã do dia <b>9 de setembro de 2025 (terça-feira)</b>, para acompanhar
        minha esposa, que se encontra em gestação, em exames médicos de rotina: ultrassonografia obstétrica e
        ecocardiograma fetal.</p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">O acompanhamento do cônjuge nesse momento é de extrema
        importância, tanto para o apoio emocional e psicológico da gestante, quanto para a participação ativa no
        acompanhamento da saúde do bebê. Ressalto ainda que tais exames possuem caráter essencial para a avaliação do
        desenvolvimento fetal e demandam a presença em horário comercial, uma vez que não há agenda disponível para a
        marcação dos exames nos fins de semana, impossibilitando sua realização fora da jornada de aula.</p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">Destaco ainda que, de acordo com a previsão do QTM desta data,
        seriam ministradas as aulas do Núcleo de Comunicações&nbsp;no período matutino&nbsp;e me comprometo a remarcar
        essas aulas em horário oportuno, o que&nbsp;<b>não acarretará prejuízo no meu aprendizado, no desempenho
            acadêmico ou na carga horária das disciplinas.</b></p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">Agradeço a compreensão e coloco-me à disposição para quaisquer
        esclarecimentos adicionais.</p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">&nbsp;</p>
    <p class="Texto_Justificado_Recuo_Primeira_Linha">Respeitosamente,</p>
    <p style="margin-top:0; margin-right:0; margin-bottom:11px; margin-left:0">&nbsp;</p>
    <p class="Nome_Signatário">Hernane Marcos de Faria Júnior, Soldado BM</p>
    <p class="Nome_Signatário">Solicitante/CFS Alfa - Turma Caparaó</p>
</body>
"""

# acessa o site do SEI
navegador.get("https://www.sei.mg.gov.br/")

# maximizar janela
navegador.maximize_window()

# inserir o meu usuário
navegador.find_element(By.ID, "txtUsuario").send_keys(user)
sleep(0.1)

# inserir minha senha
navegador.find_element(By.ID, "pwdSenha").send_keys(password)

# inserir o orgao
select_element = navegador.find_element(By.ID, "selOrgao")
select = Select(select_element)
select.select_by_visible_text(orgao)

# clicar no botão acessar
navegador.find_element(By.ID, "Acessar").click()

# clicar em Pesquisar
pesquisa = navegador.find_element(By.ID, "txtPesquisaRapida")
pesquisa.send_keys(processo)
pesquisa.send_keys(Keys.ENTER)

# mudar o frame
iframe = navegador.find_element(By.ID, "ifrVisualizacao")
navegador.switch_to.frame(iframe)

# cliar em Incluir Documento
navegador.find_element(By.CSS_SELECTOR, "#divArvoreAcoes > a:nth-child(1) > img").click()

# inserir o texto 'Oficio' na caixa de pesquisa
# pesquisa2 = navegador.find_element(By.ID, "txtFiltro").send_keys("Ofício")

# clicar em Ofício
#navegador.find_element(By.CSS_SELECTOR, "#tblSeries > tbody > tr:nth-child(52) > td > a.ancoraOpcao").click()
navegador.find_element(By.XPATH, "//a[text()='Ofício']").click()

# clicar em Público
navegador.find_element(By.CSS_SELECTOR, "#divOptPublico > div > label").click()

# clicar em Salvar
navegador.find_element(By.ID, "btnSalvar").click()
sleep(10)

# mudar a janela
janela2 = navegador.window_handles[1]
navegador.switch_to.window(janela2)

 # maximizar janela
navegador.maximize_window()

# mudar o iframe
iframe = navegador.find_element(By.CSS_SELECTOR, "#cke_4_contents > iframe")
navegador.switch_to.frame(iframe)
navegador.execute_script(f"document.body.innerHTML = `{conteudo_oficio}`")

# salvar o documento
navegador.switch_to.default_content()
sleep(2)
navegador.find_element(By.XPATH, "/html/body/form/div[1]/div[1]/div/div/span[2]/span[1]/span[3]/a").click()
sleep(2)
navegador.close()

sleep(500)