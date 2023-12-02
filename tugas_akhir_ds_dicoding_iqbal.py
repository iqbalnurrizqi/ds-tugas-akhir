# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

product_df = pd.read_csv('products_dataset.csv')
product_df.describe()
product_df.info()
product_df.isna().sum()
print("Jumlah duplikasi: ",product_df.duplicated().sum())
product_df[product_df.product_category_name.isna()]
product_df.dropna(axis=0, inplace=True)
product_df.info()
product_df.isna().sum()

products_up_df = product_df.groupby(by="product_category_name").product_id.nunique().sort_values(ascending=False)
products_up_df.head(10)

products_down_df = product_df.groupby(by="product_category_name").product_id.nunique().sort_values(ascending=True)
products_down_df.head(10)


product_df = ("cama_mesa_banho","esporte_lazer", "moveis_decoracao", "beleza_saude", "utilidades_domesticas", "automotivo", "informatica_acessorios", "brinquedos", "relogios_presentes", "telefonia")

plt.pie(
    x= products_up_df.head(10),
    labels = product_df,
    autopct='%1.1f%%',
)
st.pyplot(plt)

products_df = ("cds_dvds_musicais","seguros_e_servicos", "pc_gamer", "fashion_roupa_infanto_juvenil", "casa_conforto ", "tablets_impressao_imagem", "portateis_cozinha_e_preparadores_de_alimentos", "la_cuisine", "moveis_colchao_e_estofado", "fraldas_higiene")

plt.pie(
    x= products_down_df.head(10),
    labels = products_df,
    autopct='%1.1f%%',
)
st.pyplot(plt)



