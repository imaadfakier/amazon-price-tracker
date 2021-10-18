import requests
# import pprint
import bs4
# import lxml
import smtplib
import config

TARGET_PRICE = 60.00
# TARGET_PRICE = 51.00

url = 'enter product url'
headers = {
      # type headers here
}
response = requests.get(url=url, headers=headers)
response.raise_for_status()
website_html = response.text

soup = bs4.BeautifulSoup(markup=website_html, features='html.parser')
amazon_product_price = float(soup.find(name='span', class_='a-size-medium').get_text().split('$')[1])
amazon_product_name = soup.find(name='span', id='productTitle').string.strip()

if amazon_product_price <= TARGET_PRICE:
    with smtplib.SMTP(host=config.SMTP_SERVER_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=config.TEST_SENDER_EMAIL, password=config.TEST_SENDER_EMAIL_PASSWORD)
        email_subject_line = 'Subject:Amazon Price Alert!\n\n'
        email_subject_line = email_subject_line.encode(encoding='utf-8')
        amazon_product_info = '{product_name} is now ${product_price}\n' \
                              'Link to product: {product_purchase_link}'\
            .format(
                product_name=amazon_product_name,
                product_price=amazon_product_price,
                product_purchase_link=url
            )
        amazon_product_info = amazon_product_info.encode(encoding='utf-8')
        connection.sendmail(
            from_addr=config.TEST_SENDER_EMAIL,
            to_addrs=config.TEST_RECEIVER_EMAIL,
            msg=email_subject_line + amazon_product_info,
        )
