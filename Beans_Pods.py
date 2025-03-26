import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Déplacer st.set_page_config() en haut du script
st.set_page_config(page_title="Analyse Beans & Pods", layout="wide")

st.sidebar.title('analyse results Beans et Pods')
menu = st.sidebar.selectbox('selectionner une option', ['accueil', 'les objets'])

if menu == 'accueil':
    st.markdown("""
        <div>
            <h1> Analyse</h1>
            <p style='color:blue'>ce cours est une instruction a streamlit</p>
        </div>
    """, unsafe_allow_html=True)
elif menu == 'les objets':
    # Le reste de votre code pour 'les objets'
    st.title("Analyse des Ventes - Beans & Pods")
    # Chargement des données
    fichier = st.file_uploader("Téléchargez le fichier de données (CSV)", type=["csv"])

    if fichier is not None:
        try:
            data = pd.read_csv(fichier)

            # Aperçu des données
            st.subheader("Aperçu des données :")
            st.dataframe(data.head())

            # Analyse des ventes par canal
            st.subheader("Distribution des Ventes par Canal")
            channel_counts = data["Channel"].value_counts()
            fig_channel, ax_channel = plt.subplots()
            ax_channel.pie(channel_counts, labels=channel_counts.index, autopct="%1.1f%%", startangle=90)
            st.pyplot(fig_channel)

            # Analyse des ventes par région
            st.subheader("Distribution des Ventes par Région")
            region_counts = data["Region"].value_counts()
            fig_region, ax_region = plt.subplots()
            ax_region.pie(region_counts, labels=region_counts.index, autopct="%1.1f%%", startangle=90)
            st.pyplot(fig_region)

            # Analyse des produits (répartition et histogrammes)
            st.subheader("Analyse des Produits (Répartition et Histogrammes)")
            products = ["Robusta", "Arabica", "Espresso", "Lungo", "Latte", "Cappuccino"]
            for product in products:
                if product in data.columns:
                    st.subheader(f"Répartition des ventes de {product} par région")
                    fig_repartition, ax_repartition = plt.subplots()
                    sns.countplot(x="Region", data=data, ax=ax_repartition)
                    st.pyplot(fig_repartition)

                    st.subheader(f"Histogramme des ventes de {product} par région")
                    fig_histogram, ax_histogram = plt.subplots()
                    sns.histplot(data=data, x="Region", weights=product, ax=ax_histogram, multiple="stack")
                    st.pyplot(fig_histogram)
                else:
                    st.warning(f"La colonne '{product}' n'existe pas dans les données.")

            # Recommandations
            st.subheader("Recommandations pour la Campagne Marketing")
            st.write("""
                * **Focus sur le canal en magasin :** Les ventes dans les magasins représentent une part significative des revenus.
                * **Cibler la région [région à plus haut revenu] :** [Expliquer pourquoi cette région est importante].
                * **Promouvoir les produits [produits les plus vendus] :** Ces produits sont populaires et peuvent générer plus de ventes.
                * **Offrir des promotions ciblées :** Adapter les promotions aux préférences de chaque région et canal.
            """)

        except Exception as e:
            st.error(f"Une erreur s'est produite : {e}")

    # Rapport d'analyse et recommandations
    st.subheader("Rapport d'Analyse et Recommandations")
    st.write("""
        **Analyse des Données "Beans and Pods"**

        **Introduction**

        Beans & Pods est un fournisseur familial en pleine croissance de grains de café et de dosettes. Pour augmenter les revenus, nous avons analysé les données de vente fournies.

        **Résultats de l'Analyse**

        * [Prédominance des ventes en ligne :
          Les graphiques indiquent clairement que le canal du magasin 
           génère une part significative des ventes par rapport a celui faite en ligne. Cela suggère une forte appétence des clients pour les achats en magasin.
        **Recommandations**

        * [Liste détaillée des recommandations pour la campagne marketing, basée sur les résultats de l'analyse]
        * [L'analyse des ventes par région révèle des différences notables. Par exemple, la région « sud » pourrait se démarquer par des volumes de vente plus élevés, indiquant un marché plus porteur par rapport aux autres.]

        **Données Supplémentaires**

        * [Popularité des produits spécifiques :]
             * [Les graphiques de répartition et les histogrammes mettent en évidence les produits les plus vendus. Par exemple, « Espresso » et « Latte » pourraient être particulièrement populaires dans certaines régions comme le sud]
             * [Répartition des ventes par classe :]
             * [Les histogrammes montre la distribution des ventes pour chaque produit et par région.]
             * [Les graphiques de répartitions montrent le nombre de vente par région pour chaque produit, cela permet de voir les régions qui consomment le plus un produit et nous avons constater que tous les produit sont fortement consommer dans les region du sud et moyennement consomme dans la region du nord et faiblement consomme au centre .]
             *[Recommandations]
             *[Investir dans des campagnes de marketing numérique ciblées (publicités sur les réseaux sociaux, référencement payant) pour augmenter le trafic sur le site web]
             
        **Conclusion**

        En suivant ces recommandations, Beans & Pods peut optimiser sa campagne marketing et augmenter ses revenus.
    """)
     # Lien GitHub
    st.markdown("Lien GitHub : (https://github.com/jospin646/Projet1IA1")

   
