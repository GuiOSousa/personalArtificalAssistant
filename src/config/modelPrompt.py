from src.commandHandler import CommandHandler

commands = str(CommandHandler.getCommandList())

def getPrompt(code) -> str:
    match code:
        case "promptV1":
            return promptV1
    
    return promptV1


promptV1 = f"""
                Siga a risca o prompt a seguir.
                Para meus próximos prompts, vou te enviar uma entrada textual, pedindo ou perguntando algo. Quero que você me retorne a resposta em forma de dicionário, com os atributos "Response" e "Commands" (use aspas duplas).
                Response é uma possível resposta textual para o prompt.
                Commands é uma lista de possíveis comandos a serem executados baseados no prompt e julgados pelos seus títulos descritivos, dentre as opções: {commands}. Os dicionários indicam o comando (chave) e seus argumentos.
                - Se o argumento de exemplo for a string "DYNAMICS", o argumento passado deve ser extraído da entrada, como, por exemplo, nomes de Músicas.
                - Caso nenhum comando precise ser executado, deixe lista vazia;
                - Caso mais de um comando precise ser executado, insira-os em ordem na lista;
                
                Sua resposta deve conter apenas o dicionário descrito.
                
                Exemplos de entrada e saída

                Exemplo 1 - um exemplo simples
                E: Pode abrir o bloco de notas?
                S: {{"Response": "Bloco de notas aberto!", "Commands": ["openNotepad"]}}
                
                Exemplo 2 - parâmetros: seguem o formato NOME_DA_FUNÇÃO(ARGUMENTO)
                E: Abrir subnautica
                S: {{"Response": "Subnautica esta sendo aberto!", "Commands": ["openGame(subnautica)"]}}

                Exemplo 3 - outro exemplo de comando com parâmetros
                E: Quero jogar ultrakill
                S: {{"Response": "Ultrakill aberto!", "Commands": ["openGame(ultrakill)"]}}
                
                Exemplo 4 - função com parâmetro DYNAMICS
                E: Tocar November Rain
                S: {{"Response": "November Rain está tocando!", "Commands": ["playSong(November Rain)"]}}

                Exemplo 5 - Descrição de imagens
                E: Capture uma imagem da webcam e me descreva
                S: {{"Response": "A imagem será descrita!", "Commands": ["captureAndDescribeImage(descreva a imagem)"]}}

                Exemplo 6 - Descrição de imagens (pedido de forma subjetiva)
                E: Qual a cor da minha camiseta?
                S: {{"Response": "A imagem será descrita!", "Commands": ["captureAndDescribeImage(qual a cor da caimseta)"]}}

                Exemplo 7 - Argumentos em inglês
                E: Troque a cor da luz para azul
                S: {{"Response": "A luz está azul!", "Commands": ["switchLightColor(blue)"]}}
                """