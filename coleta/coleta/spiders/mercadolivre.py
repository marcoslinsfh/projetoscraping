import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ['https://lista.mercadolivre.com.br/tenis-corrida-masculino']
    pag_inicial = 1
    pag_final = 20

    def parse(self, response):
        produtos = response.css('div.ui-search-result__content')
      

        for produto in produtos: 
            
            precos = produto.css('span.andes-money-amount__fraction::text').getall()
            centavos = produto.css('span.andes-money-amount__cents::text').getall()

            yield {
                'brand': produto.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
                'titulo': produto.css('h2.ui-search-item__title::text').get(),
                'avaliacao': produto.css('span.ui-search-reviews__rating-number::text').get(),
                'qtd_avaliacao': produto.css('span.ui-search-reviews__amount::text').get(),
                'anunciante': produto.css('p.ui-search-official-store-label.ui-search-item__group__element.ui-search-color--GRAY::text').get(), 
                'preco_antes': precos[0] if len(precos) > 0 else None,
                'preco': precos[1] if len(precos) > 1 else None,
                'preco_antes_cents': centavos[0] if len(centavos) > 0 else None,
                'preco_cents': centavos[1] if len(centavos) > 1 else None,
                'promocao': produto.css('span.ui-search-price__discount::text').get(),
                'frete': produto.css('span.ui-pb-highlight::text').get()
            }
            
        if self.pag_inicial < self.pag_final:
            prox_pag = response.css ('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if prox_pag:
                self.pag_inicial += 1
                yield scrapy.Request (url=prox_pag, callback=self.parse)

