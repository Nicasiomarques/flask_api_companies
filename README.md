## API de Gerenciamento de Empresas

Este projeto consiste no desenvolvimento de endpoints para realizar operações de CRUD (Create, Read, Update, Delete) em registros de empresas, utilizando a linguagem de programação Python e o framework web Flask. Os endpoints permitem cadastrar, editar, remover e listar empresas, oferecendo suporte à paginação, ordenação e limite de registros por página.

### Requisitos

1. **Cadastro de Nova Empresa**: Endpoint para cadastrar uma nova empresa com os campos obrigatórios: CNPJ, Nome Razão, Nome Fantasia e CNAE.
2. **Edição de Empresa Existente**: Endpoint para editar um cadastro de empresa existente, permitindo alterar apenas os campos Nome Fantasia e CNAE.
3. **Remoção de Empresa**: Endpoint para remover um cadastro de empresa existente com base no CNPJ.
4. **Listagem de Empresas**: Endpoint de listagem de empresas, com suporte à paginação, ordenação e limite de registros por página.

### Dicas e Observações

- Utilize o framework web Flask para a criação dos endpoints.
- Para a listagem paginada, utilize os parâmetros (start, limit, sort e dir) para especificar os critérios de paginação e ordenação.
- Documente os endpoints utilizando o Swagger ou outra ferramenta de documentação de endpoints.

### Bônus (opcional)

Caso queira adicionar mais complexidade ao projeto, você pode considerar as seguintes melhorias:

1. **Validações nos Campos de Entrada**: Implementar validações nos campos de entrada, como verificação de formato de CNPJ válido.
2. **Autenticação e Autorização**: Adicionar autenticação e autorização aos endpoints para garantir que apenas usuários autorizados possam realizar as operações CRUD.
3. **Banco de Dados Relacional**: Utilizar um banco de dados relacional (por exemplo, SQLite, PostgreSQL) para armazenar os dados das empresas, criando a estrutura do banco e as migrações necessárias.

## Configuração do Ambiente

Antes de executar o projeto, certifique-se de configurar corretamente o ambiente através do arquivo `.env`. Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes variáveis com seus respectivos valores:

```plaintext
DATABASE_PATH=sqlite:////tmp/companyDB.db
JWT_SECRET_KEY=38H49UH3FRUGHOIGHEROBGOFDUBGJOBDKFJBGDOFOBOGUBEJBG
JWT_EXPIRES_DAY=1
```

Essas variáveis são necessárias para o funcionamento correto do Flask e do JWT.

## Executando o Projeto Localmente

Siga as etapas abaixo para executar o projeto em sua máquina local.

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Nicasiomarques/flask_api_companies.git
   cd flask_api_companies
   ```

2. **Configuração do ambiente virtual (opcional)**:

   É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto. Use o `venv`, `virtualenv` ou outra ferramenta de sua preferência:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do banco de dados**:

   Antes de executar o projeto, configure o banco de dados em `config.py` e aplique as migrações:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Inicie o servidor de desenvolvimento**:

   ```bash
   flask run
   ```

   O servidor estará acessível em `http://localhost:5000`.

## Autenticação

Para acessar as rotas protegidas da empresa, é necessário primeiro obter um token JWT através do endpoint de autenticação.

### Login de Usuário

Realiza o login de um usuário e retorna um token JWT válido para acesso às rotas protegidas.

- **URL:** `/auth/login`
- **Método:** `POST`
- **Corpo da Requisição (JSON):**
  - `username` (string, obrigatório): Nome de usuário.
  - `password` (string, obrigatório): Senha do usuário.

##### Exemplo de Uso com `curl`:

```bash
curl -X POST \
  http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "seu_usuario",
    "password": "sua_senha"
  }'
```

O resultado será um JSON contendo o token JWT:

```json

{
	"id": 2,
	"password": "$pbkdf2-sha256$29000$pNRaK2Us5fyf0zpnjLGWcg$2H96fvJCMknJdaY4dhYoc9sns0WND1j82pRvGELkNa4",
	"username": "nick123",
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDM2NDY5MiwianRpIjoiYWUyNGE1YWQtYTE3ZS00NDc2LWFhY2EtNTRkMGY3MGFkNTI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNjkwMzY0NjkyLCJleHAiOjE2OTA0NTEwOTJ9.2uqt0KyvFS1gv7JnBEp6SsYxCcYG8iPuQQqOEgpdBzs",
	"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDM2NDY5MiwianRpIjoiZDg5N2EyMDMtYTFiOS00ZjMzLTk2Y2MtMGQxNTA3MjZjNmI0IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjIsIm5iZiI6MTY5MDM2NDY5MiwiZXhwIjoxNjkyOTU2NjkyfQ.XVyS56Ev0TO7JicxsY-B0tRpsy8uruUWUt5Mr

POiSKE"
}

```

### Registro de Novo Usuário

Registra um novo usuário na aplicação.

- **URL:** `/auth/signup`
- **Método:** `POST`
- **Corpo da Requisição (JSON):**
  - `username` (string, obrigatório): Nome de usuário.
  - `password` (string, obrigatório): Senha do usuário.

##### Exemplo de Uso com `curl`:

```bash
curl -X POST \
  http://localhost:5000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "username": "novo_usuario",
    "password": "nova_senha"
  }'
```

### Endpoints da Empresa

Aqui estão os endpoints disponíveis na API para a empresa:

#### Listar Todas as Empresas

Retorna uma lista paginada contendo todas as empresas cadastradas.

- **URL:** `/companies`
- **Método:** `GET`
- **Parâmetros da URL (opcionais):**
  - `page` (int): Página atual (padrão: 1).
  - `per_page` (int): Número de itens por página (padrão: 25).
  - `order` (string): Campo pelo qual os resultados serão ordenados (opcional).
- **Header da Requisição:**
  - `Authorization`: Token JWT obtido no login.

##### Exemplo de Uso com `curl`:

```bash
curl -X GET \
  http://localhost:5000/companies \
  -d "page=1" \
  -d "per_page=10" \
  -d "order=nome_fantasia" \
  -H "Authorization: Bearer seu-token-jwt"
```

#### Adicionar uma Nova Empresa

Adiciona uma nova empresa ao banco de dados.

- **URL:** `/companies`
- **Método:** `POST`
- **Corpo da Requisição (JSON):**
  - `name` (string, obrigatório): Nome da empresa.
  - `cnae` (string, obrigatório): Código Nacional de Atividade Econômica (CNAE) da empresa.
  - `fantasyName` (string, obrigatório): Nome fantasia da empresa.
  - Outros campos opcionais, se aplicável.
- **Header da Requisição:**
  - `Authorization`: Token JWT obtido no login.

##### Exemplo de Uso com `curl`:

```bash
curl -X POST \
  http://localhost:5000/companies \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-jwt" \
  -d '{
    "name": "Empresa XYZ",
    "cnae": "123456",
    "fantasyName": "Empresa Fantasia"
  }'
```

#### Obter Detalhes de uma Empresa

Retorna os detalhes de uma empresa específica com base no ID fornecido.

- **URL:** `/companies/<int:id>`
- **Método:** `GET`
- **Parâmetro da URL:**
  - `id` (int): ID da empresa a ser obtida.
- **Header da Requisição:**
  - `Authorization`: Token JWT obtido no login.

##### Exemplo de Uso com `curl`:

```bash
curl -X GET http://localhost:5000/companies/1 -H "Authorization: Bearer seu-token-jwt"
```

#### Editar uma Empresa

Edita os campos "cnae" e "fantasyName" de uma empresa específica com base no ID fornecido.

- **URL:** `/companies/<int:id>`
- **Método:** `PUT`
- **Parâmetro da URL:**
  - `id` (int): ID da empresa a ser editada.
- **Corpo da Requisição (JSON):**
  - `cnae` (string, obrigatório): Novo CNAE da empresa.
  - `fantasyName` (string, obrigatório): Novo nome fantasia da empresa.
- **Header da Requisição:**
  - `Authorization`: Token JWT obtido no login.

##### Exemplo de Uso com `curl`:

```bash
curl -X PUT \
  http://localhost:5000/companies/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-jwt" \
  -d '{
    "cnae": "987654",
    "fantasyName": "Novo Nome Fantasia"
  }'
```

#### Excluir uma Empresa

Exclui uma empresa específica com base no CNPJ fornecido.

- **URL:** `/companies/<string:cnpj>`
- **Método:** `DELETE`
- **Parâmetro da URL:**
  - `cnpj` (string): CNPJ da empresa a ser excluída.
- **Header da Requisição:**
  - `Authorization`: Token JWT obtido no login.

##### Exemplo de Uso com `curl`:

```bash
curl -X DELETE http://localhost:5000/companies/CNPJ-da-Empresa -H "Authorization: Bearer seu-token-jwt"
```

## Possíveis Melhorias (Não Implementadas)

Embora o projeto já tenha sido desenvolvido com sucesso, existem algumas melhorias que poderiam ser adicionadas para torná-lo ainda mais robusto e escalável. Algumas dessas melhorias incluem:

1. **SOLID Principles**: Refatoração do código para aderir aos princípios SOLID, que promovem uma estrutura de código mais modular, flexível e de fácil manutenção.

2. **Clean Architecture**: Implementação da Clean Architecture, que separa o código em camadas com responsabilidades bem definidas, facilitando a escalabilidade e a substituição de tecnologias sem afetar a lógica de negócio.

3. **Hexagonal Architecture**: Adoção da Hexagonal Architecture (também conhecida como Ports and Adapters), que permite isolar a lógica de negócio da infraestrutura, tornando o projeto mais independente e testável.

4. **Testes Automatizados**: Desenvolvimento de testes automatizados (testes unitários, testes de integração, etc.) para garantir a qualidade do código e prevenir regressões.

5. **Graceful Shutdown**: Implementação de um mecanismo de "Graceful Shutdown" para a API, garantindo que todas as conexões e processos sejam finalizados corretamente ao encerrar o serviço.

6. **Health Check**: Adição de endpoints de "Health Check" para monitorar o estado da aplicação, possibilitando a detecção precoce de problemas e a tomada de ações corretivas.

7. **Contêinerização Docker**: Criação de um Dockerfile para empacotar a aplicação em um contêiner, facilitando a implantação e a garantia de que a aplicação funcione de forma consistente em diferentes ambientes.

8. **Orquestração com Kubernetes**: Utilização do Kubernetes para orquestrar e gerenciar os contêineres da aplicação em um ambiente de produção, tornando a implantação e o dimensionamento mais eficientes.

9. **Caching de Rotas Pesadas**: Implementação de caching para rotas que realizam consultas pesadas ou cálculos intensivos, melhorando o desempenho e reduzindo a carga no banco de dados.

10. **Rate Limit e Slowdown**: Adoção de rate limiting para limitar o número de requisições por IP ou usuário, e slowdown para controlar a taxa de resposta em momentos de alto tráfego.

É importante ressaltar que essas melhorias são consideradas opcionais e podem depender dos requisitos específicos do projeto e dos recursos disponíveis. Ao implementar essas melhorias, o projeto se tornará mais robusto, seguro e escalável, proporcionando uma melhor experiência tanto para os usuários como para os desenvolvedores que trabalham nele.

## Como Contribuir

Agradecemos seu interesse em contribuir para o projeto! Contribuições são sempre bem-vindas e podem ajudar a melhorar a qualidade e funcionalidade da API de Gerenciamento de Empresas. Abaixo estão algumas diretrizes sobre como contribuir:

### 1. Abrindo Issues

Se você encontrou um bug, deseja sugerir uma melhoria ou tem alguma dúvida sobre o projeto, sinta-se à vontade para abrir uma issue no repositório. Descreva claramente o problema ou a sugestão para que possamos entender melhor a questão e respondê-la adequadamente.

### 2. Realizando Fork e Pull Requests

Se você deseja contribuir com código para o projeto, siga os passos abaixo:

1. Faça um fork do repositório para o seu próprio perfil do GitHub.
2. Clone o repositório forkado para o seu ambiente local.
3. Crie um branch para suas alterações:

   ```bash
   git checkout -b nome-da-sua-feature
   ```

4. Realize as alterações desejadas no código e adicione os commits de forma coerente.

### Git Flow e Convenção de Commits

Para manter um fluxo de trabalho organizado, recomendamos seguir o Git Flow e a Convenção de Commits.

#### Git Flow

O Git Flow é uma metodologia de organização de branches que ajuda a gerenciar as diferentes etapas do desenvolvimento. Seguindo essa abordagem, temos dois branches principais:

- `main`: Branch principal que contém o código estável do projeto. Commits direcionados a esse branch devem ser feitos por meio de Pull Requests.

- `develop`: Branch de desenvolvimento que contém o código em andamento. Os novos recursos e correções de bugs devem ser feitos a partir dessa branch.

Além disso, para cada nova funcionalidade ou correção, é recomendável criar um branch a partir do `develop` e dar um nome descritivo, como `feature/nome-da-funcionalidade` ou `bugfix/nome-do-bug`. Quando a funcionalidade ou correção estiver pronta, você pode abrir um Pull Request para mesclar as alterações no `develop`.

#### Convenção de Commits

Uma boa convenção de commits ajuda a manter um histórico de alterações claro e consistente. Recomendamos seguir o formato Conventional Commits. Isso implica em começar o commit com um dos seguintes prefixos:

- `feat`: Para adicionar uma nova funcionalidade.
- `fix`: Para correção de bugs.
- `chore`: Para alterações de configurações e tarefas de manutenção.
- `docs`: Para alterações na documentação.
- `style`: Para alterações de formatação ou estilo que não afetam o código em si.
- `refactor`: Para alterações de código que não adicionam novas funcionalidades nem corrigem bugs.
- `test`: Para adição ou modificação de testes.

Exemplo de um commit usando a convenção:

```
feat: Adiciona endpoint de listagem de empresas
```

### 3. Abra um Pull Request

Quando suas alterações estiverem prontas, abra um Pull Request para o branch `develop`. Descreva claramente o que foi alterado e adicione qualquer informação relevante. Seu Pull Request será revisado e, se estiver tudo certo, será mesclado ao branch `develop`.

### 4. Manutenção Contínua

Após a mesclagem do seu Pull Request, o projeto continuará evoluindo e você pode continuar contribuindo com novas funcionalidades e correções sempre que desejar.

Lembre-se de sempre manter um ambiente de respeito e colaboração ao contribuir para o projeto. Sua ajuda é valiosa e é graças à comunidade que o projeto pode crescer e se aprimorar. Seja bem-vindo(a) à equipe de contribuidores(as) deste projeto!
