import json
import pandas as pd
import time
import requests
import random
import time
import boto3
from datetime import datetime
import datetime
import os

# Configura el cliente S3 de AWS
s3_client = boto3.client('s3')

# Función para obtener estadísticas de un canal de YouTube
def get_stats(api_key, channel_id):
    # Construye la URL para obtener estadísticas del canal
    url_channel_stats = 'https://'+channel_id+'&key='+api_key
    response_channels = requests.get(url_channel_stats)
    channel_stats = json.loads(response_channels.content)
    channel_stats = channel_stats['items'][0]['statistics']
    date = pd.to_datetime('today').strftime("%Y-%m-%d")

    data_channel = {
        'Date': date,
        'Total_Views': int(float(channel_stats['viewCount'])),
        'Subscribers': int(float(channel_stats['subscriberCount'])),
        'Video_count': int(float(channel_stats['videoCount']))
    }

    return data_channel

# Función para obtener estadísticas de varios canales
def channels_stats(df, api_key):
    date = []
    views = []
    subscriber = []
    video_count = []
    channel_name = []
    
    tiempo = [1, 2.5, 2]
    
    for i in range(len(df)):
        # Obtiene estadísticas de un canal
        stats_temp = get_stats(api_key, df['Channel_id'][i])
        
        channel_name.append(df['Channel_name'][i])
        date.append(stats_temp['Date'])
        views.append(stats_temp['Total_Views'])
        subscriber.append(stats_temp['Subscribers'])
        video_count.append(stats_temp['Video_count'])
     
    time.sleep(random.choice(tiempo))
    
    data = {
        'Channel_name': channel_name,
        'Subscribers': subscriber,
        'Video_count': video_count,
        'Total_Views': views,
        'Created_at': date,
    }
    
    df_channels = pd.DataFrame(data)
    
    return df_channels

# Función principal de AWS Lambda
def lambda_handler(event, context):
    bucket_name = os.environ['BUCKET_INPUT']
    filename = os.environ['FILE_CHANNELS']
    DEVELOPER_KEY = os.environ['APIKEY']
    
    # Obtiene el archivo CSV desde S3
    obj = s3_client.get_object(Bucket=bucket_name, Key=filename)
    df_channels = pd.read_csv(obj['Body'])
    
    # Obtiene las estadísticas de los canales
    results = channels_stats(df_channels, DEVELOPER_KEY)
    date = pd.to_datetime('today').strftime("%Y%m%d")
    
    # Guarda las estadísticas en un archivo CSV temporal
    results.to_csv(f'/tmp/youtube_stats_{date}.csv', index=False)
 
    # Sube el archivo CSV a S3
    s3 = boto3.resource("s3")
    s3.Bucket(os.environ['BUCKET_DESTINY']).upload_file(f'/tmp/youtube_stats_{date}.csv', Key=f'youtube_stats_{date}.csv')
    os.remove(f'/tmp/youtube_stats_{date}.csv')

    return f'file youtube_stats_{date}.csv send succeeded'
