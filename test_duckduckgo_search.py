from selene import browser, be, have


def test_search_open_duckduckgo():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('qa guru').press_enter()
    browser.element('a[href^="https://qa.guru/"]').should(be.clickable).click()

def test_search_negative_duckduckgo():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('ghvbnwww').press_enter()
    browser.element('html').should(have.text('По запросу ghvbnwww ничего не найдено'))