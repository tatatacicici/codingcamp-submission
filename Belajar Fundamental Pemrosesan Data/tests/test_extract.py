import pytest
import pandas as pd
import requests.exceptions
from bs4 import BeautifulSoup

from utils.extract import parse_product
from unittest.mock import patch, Mock

def test_fetch_page_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b"<html>Test</html>"
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        from utils.extract import fetch_page
        content = fetch_page("https://test.com")
        assert content == b"<html>Test</html>"
def test_fetch_page_failure():
    with patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error")):
        from utils.extract import fetch_page
        content = fetch_page("https://test.com")
        assert content is None
def test_parse_product_data():
    mock_html = """
        <div class="collection-card">
            <div class="product-details">
                <h3 class="product-title">T-shirt 2</h3>
                <div class="price-container">
                    <span class="price">$102.15</span>
                </div>
                <p style="font-size: 14px; color: #777;">Rating: ⭐ 3.9 / 5</p>
                <p style="font-size: 14px; color: #777;">3 Colors</p>
                <p style="font-size: 14px; color: #777;">Size: M</p>
                <p style="font-size: 14px; color: #777;">Gender: Women</p>
            </div>
        </div>
        """
    soup = BeautifulSoup(mock_html, "html.parser")
    article = soup.select_one('.collection-card')

    product_data = parse_product(article)

    assert product_data is not None

def test_scrape_main_success():
    mock_html = """
    <div class="collection-card">
        <div class="product-details">
            <h3 class="product-title">Test Shirt</h3>
            <div class="price-container"><span class="price">$45.00</span></div>
            <p>Rating: ⭐ 4.5 / 5</p>
            <p>2 Colors</p>
            <p>Size: L</p>
            <p>Gender: Men</p>
        </div>
    </div>
    """

    with patch("utils.extract.fetch_page", return_value=mock_html.encode("utf-8")):
        from utils.extract import scrape_main
        df = scrape_main(base_url="https://test.com", total_pages=1, delay=0)

        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert df.iloc[0]["Title"] == "Test Shirt"
