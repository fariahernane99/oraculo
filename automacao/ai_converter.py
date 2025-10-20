# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

def make_response(prompt: str) -> str:
  print('entrou make_response')
  GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('models/gemini-2.0-flash-lite')
  prompt_aux = "Baseado no texto a seguir, crie um texto de ofício de resposta seguindo a seguinte estrutura: Deve ser retornado apenas um texto em formato de lista, conforme o exemplo: '[<resposta>, <resposta>, <resposta>]', com no máximo 3 parágrafos. Não se esqueça de retornar apenas a lista em texto, pois irei convertê-la para uma lista de python posteriormente. Segue o texto a ser analisado: "
  prompt = prompt_aux + prompt
  response = model.generate_content(prompt)
  response = eval(response.text)  # Convertendo a string de volta para uma lista
  print('saiu make_response')
  return response

if __name__ == "__main__":
  prompt = "Prezado Senhor, Venho por meio deste solicitar, em nome deste batalhão, a disponibilização de computadores para uso administrativo e operacional. Ressaltamos que a aquisição desses equipamentos é fundamental para aprimorar a eficiência dos trabalhos, garantir a segurança das informações e atender às demandas crescentes das atividades militares. Solicitamos, portanto, a gentileza de informar sobre a possibilidade de atendimento a esta solicitação, bem como os procedimentos necessários para viabilizar o fornecimento dos computadores. Certos de sua atenção e colaboração, agradecemos antecipadamente. Respeitosamente Hernane Marcos de Faria Júnior SD BM SECOM do 9ºBBM"
  resposta = make_response(prompt)
  print(resposta)