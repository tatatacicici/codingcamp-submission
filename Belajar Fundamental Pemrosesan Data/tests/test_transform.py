
import pytest
import pandas as pd
from utils.transform import clean_data, clean_price, clean_rating, clean_colors, clean_size, clean_gender, validate_title, transform_data

def test_clean_data():
    shop_df = pd.DataFrame({
        'Title': ['T-shirt', 'T-shirt', None],
        'Price': ['$10', '$10', '$20']
    })
    result = clean_data(shop_df)
    assert len(result) == 1
    assert result.iloc[0]['Title'] == 'T-shirt'

    #test dataframe kosong
    empty_df = pd.DataFrame({'Title': [None], 'Price': [None]})
    with pytest.raises(ValueError, match='DataFrame menjadi kosong setelah membersihkan duplikat dan nilai null'):
        clean_data(empty_df)
def test_clean_price():
    assert clean_price('$10.50') == 10.50 * 16000
    assert clean_price('Price Unavailable') is None
    assert clean_price(None) is None
    assert clean_price("") is None
def test_clean_rating():
    assert clean_rating('3.9') == 3.9
    assert clean_rating('Invalid Rating') is None
    assert clean_rating('Not Rating') is None
    assert clean_rating(None) is None
def test_clean_colors():
    assert clean_colors('3 Colors') == 3
    assert clean_colors(None) is None
def test_clean_size():
    assert clean_size('Size: M') == 'M'
    assert clean_size(None) is None
def test_clean_gender():
    assert clean_gender('Gender: Women') == 'Women'
    assert clean_gender('Unknown') is None
    assert clean_gender(None) is None
def test_validate_title():
    assert validate_title('T-shirt 2') == 'T-shirt 2'
    assert validate_title('Unknown Product') is None
    assert validate_title(None) is None


def test_transform_data():
    df = pd.DataFrame({
        'Title': ['T-shirt 2', 'Unknown Product'],
        'Price': ['$10.50', '$20'],
        'Rating': ['3.9', 'Invalid Rating'],
        'Colors': ['3 Colors', 'Unknown Colors'],
        'Size': ['Size: M', 'Size: Unknown'],
        'Gender': ['Gender: Women', 'Gender: Unknown'],
        'Timestamp': ['2025-05-06 12:00:00', '2025-05-06 12:00:00']
    })

    result = transform_data(df)

    assert len(result) == 1
    assert result.iloc[0]['Title'] == 'T-shirt 2'
    assert result.iloc[0]['Price'] == 10.50 * 16000
    assert result.iloc[0]['Rating'] == 3.9
    assert result.iloc[0]['Colors'] == 3
    assert result.iloc[0]['Size'] == 'M'
    assert result.iloc[0]['Gender'] == 'Women'
    assert result.dtypes['Title'] == 'object'
    assert result.dtypes['Price'] == 'float64'
    assert result.dtypes['Colors'] == 'int64'


def test_transform_data_empty():
    df = pd.DataFrame({
        'Title': ['Unknown Product'],
        'Price': ['Price Unavailable'],
        'Rating': ['Invalid Rating/5'],
        'Colors': [None],
        'Size': [None],
        'Gender': ['Unknown'],
        'Timestamp': ['2025-05-06 12:00:00']
    })

    with pytest.raises(ValueError, match="Gagal transformasi data: Gagal membersihkan data"):
        transform_data(df)


