from flask import Blueprint, render_template
import json
from google.cloud import datastore

get_country_data_bp = Blueprint('get_country_data', __name__)

@get_country_data_bp.route('/country-data')
def country_population():
    client = datastore.Client()
    countries = []
    for country_code in ['MY', 'VN', 'PH', 'TH', 'SG', 'KH', 'MM', 'BN', 'LA', 'ID']:
        query = client.query(kind='country')
        query.add_filter('country_code', '=', country_code)
        query.order = ['-timestamp']
        query.limit = 1
        result = list(query.fetch())
        if result:
            country = {
                'code' : result[0]['country_code'],
                'name': result[0]['country_name'],
                'population': result[0]['population'],
                'timestamp': result[0]['timestamp']
            }
            countries.append(country)
    return render_template('country_population.html', countries=countries)

@get_country_data_bp.route('/country-chart')
def country_population_chart():
    client = datastore.Client()
    countries = []
    for country_code in ['MY', 'VN', 'PH', 'TH', 'SG', 'KH', 'MM', 'BN', 'LA', 'ID']:
        query = client.query(kind='country')
        query.add_filter('country_code', '=', country_code)
        query.order = ['-timestamp']
        query.limit = 1
        result = list(query.fetch())
        if result:
            country = {
                'code' : result[0]['country_code'],
                'name': result[0]['country_name'],
                'population': result[0]['population'],
                'timestamp': result[0]['timestamp']
            }
            countries.append(country)
    return render_template('country_population_chart.html', countries=countries)

