# projetoscraping

Para rodar o WebScraping no ML

```bash 
scrapy crawl mercadolivre -o ../data/data.jsonl
```

Para rodar o ETL com o PANDAS a partir da pasta base do projeto

```bash 
python transformacao/main.py
```

Para rodar o Streamlit para criar o dashboard

```bash 
streamlit run dashboard/app.py
```