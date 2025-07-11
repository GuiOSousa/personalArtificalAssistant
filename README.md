# Asistente Pessoal Artificial
O Assistente Pessoal Artifical (APA) é um assistente baseado em LLM com capacidade de executar tarefas variadas. A ideia é combinar comandos de voz, um modelo LLM e um conjunto de funções para realizar ações como abrir aplicativos no computador, acessar câmeras ou ligar luzes.

Um dos principais objetivos do projeto (e a principal razão para o uso de uma LLM) é que esses comandos de voz possam ser completamente naturais. "Abrir Google Chrome" e "Por favor, você poderia abrir o google?" essencialmente requisitam, semanticamente, a mesma tarefa, apesar da diferença de sintaxe.

Na versão atual (v0.2.0) o APA é capaz de *abrir programas* no computador, *ligar/desligar luzes* e *tocar músicas no Spotify*.

*Importante*: Leia o tópico 6 sobre a execução do projeto.
## 1 - Comandos de Voz
A voz do usuário é capturada para extrair os comandos ou perguntas.

### 1.1 - VoiceHandler
O *VoiceHandler* é responsável por capturar o áudio do usuário e transcrevê-lo em forma de texto. Esse texto então é passado para o *VoiceCommandInterpreter*

### 1.2 - VoiceCommandInterpreter
Recebendo uma entrada de texto, o *VoiceCommandInterpreter* será responsável por se comunicar com a LLM e o executor de comandos.
Primeiro, ele envia a entrada para o *LanguageModel*, que o retornará um dicionário. A chave "Commands" então é dada como entrada para o *CommandHandler*, responsável pela execução dos comandos.

## 2 - LLM
Um Large Language Model é utilizado para interpretar a entrada textual e arquitetar as ações a serem executadas.

### 2.1 - LanguageModel
Recebendo uma entrada de texto do *VoiceCommandInterpreter* o *LanguageModel* vai interpretar o texto e montar um dicionário com 2 chaves: "Response" e "Commands".

Response é uma resposta textual para o comando, confirmando a execução das tarefas ou respondendo a pergunta do usuário.

Commands é uma lista de possíveis comandos a serem executados, escolhidos pelo *LanguageModel* por seus nomes descritivos, dentre as opções de comandos do *CommandHandler*.

## 3 - Execução de Comandos
Uma lista de comandos é recebida e cada comando é executado sequencialmente.

### 3.1 - CommandHandler
Após receber a lista de comandos do *VoiceCommandInterpreter*, em forma de strings, o *CommandHandler* faz um match com os nomes das funções e as executa sequencialmente utilizando o *CommandExecuter*

### 3.2 - CommandExecuter
Responsável por executar os comandos requisitados pelo *CommandHandler*.

## 4 - Comandos
Os comandos são a parte mais abrangente da aplicação. São eles que, de fato, definem a escalabilidade do projeto, sendo o foco de futuras atualizações.

Contam com nomes descritivos e diretos, para facilitar a escolha do *LanguageModel*. Os comandos disponíveis estão listados no tópico 7.


## 5 - Exemplos
Os exemplos contam com uma entrada (o que foi dito para o *VoiceHandler*) e a saída do *LanguageModel*, contendo a resposta textual (R) e a lista de comandos (C). Caso a entrada do *LanguageModel* não requira comandos, nenhum comando será executado.

* "Abra o Google" -> R: "O Google Chrome foi aberto!"; C: ["openGoogleChrome"].

* "Qual o estado mais populoso do Brasil?" -> R: "O estado mais populoso do Brasil é São Paulo"; C: [""]

* "Você pode abrir o bloco de notas, por favor?" -> R: "Bloco de notas aberto!"; C: ["openNotepad"]

* "Acenda as luzes" -> R: "As luzes foram acessas!"; C: ["turnOnLight"]

* "Tocar Smells Like Teen Spirit" -> R: "Tocando Smells Like Teen Spirit"; C: ["playSong(Smells Like Teen Spirit)"]

## 6 - Execução
As bibliotecas necessárias estão disponíveis no arquivo requirements.txt. Para instalá-las, execute o comando:

`pip install -r requirements.txt`

Um modelo de local LLM também será necessário.

O projeto utiliza o modelo"Meta-Llama-3-8B-Instruct.Q4_0", instalado separadamente na pasta `models` dentro da pasta `src`. O modelo pode ser baixado gratuitamente via GPT4All e inserido na pasta. Devido ao tamanho extenso do arquivo, ele não foi inserido no repositório.

*Obs: Apesar do programa apontar os erros `Failed to load llamamodel-mainline-cuda-avxonly.dll: LoadLibraryExW failed with error 0x7e` e `Failed to load llamamodel-mainline-cuda.dll: LoadLibraryExW failed with error 0x7e` ao executar, ele funciona normalmente. A lentidão do processo será investidada nas próximas atualizações*

Lâmpadas requerem configurção adicional. Neste projeto, uma lâmpada RGB compatível com Tuya foi usada.

A Intergração com Spotify exige uma conta Premium e credenciais válidas de API.

A Integração com o Google AI Studio (descrição de imagens capturadas) exige uma API Key válida.

## 7 - Lista de Comandos
- openNotepad() - Abre o bloco de notas
- openGoogleChrome() - Abre o Google
- openGame(gameName) - Abre um jogo na Steam, dentre as opções disponíveis.
- turnOnLight() - Liga a lâmpada configurada
- turnOffLight() - Desliga a lâmpada configurada
- playSong(songTitle) - Toca a música passada no Spotify
- addSongToQueue(songTitle) - Adiciona a música passada na fila do Spotify
- captureAndSaveImage() - Captura uma imagem da WebCam e salva na pasta "savedFiles"
- captureAndDescribeImage() - Captura uma imagem da WebCam e descreve-a baseando-se no prompt mandado. (Esta funcionalidade ainda está sendo testada)


## 8 - Versões
### v0.1.0 (23/05/2025)
- Primeira versão lançada.

### v0.1.1 (25/05/2025)
- Novos comandos (1)
- Introdução de comandos com parâmetros.
- Pequenas correções no tempo de espera da detecção de voz.

### v0.1.2 (31/05/2025)
- Novos comandos (2)
- Interação com dispositivos Tuya (lâmpada RGB)

### v0.2.0 (05/06/2025)
- Novos comandos (2)
- Introdução de comandos com argumentos dinâmicos.
- Contexto Ativo: O programa aceita várias entradas em sequência sem precisar ser reiniciado.
- Integração com Spotify

### v0.2.1 (13/06/2025)
- Novos comandos (2)
- Captura de imagens
- Integração com Google AI Studio para descrição de imagens.