import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Changer les datasets de Seaborn
dataset = {
    "flights": sns.load_dataset("flights"),
    "tips": sns.load_dataset("tips"),
    "iris": sns.load_dataset("iris"),
}

# Affichage du titre avec du HTML et du CSS
st.markdown(
    """
    <h1 style="color: blue;">STREAMLIT_2</h1>
    <h2 style="color: red;">Manipulations des données et création des graphiques associés</h2>
    """, unsafe_allow_html=True
)

# Choisir le dataset
dataset_name = st.selectbox("Quel dataset souhaitez-vous voir ? : ", list(dataset.keys()))
df = dataset[dataset_name]

# Affichage du dataset
st.write("On obtient : ", df)

# Choix des colonnes X et Y
columns = list(df.select_dtypes(include=["number", "category"]).columns)
x_col = st.selectbox("Choix colonne X", columns)
y_col = st.selectbox("Choix colonne Y", columns)

# Choix du graphique
chart_type = st.selectbox(
    "Quel graphique souhaitez-vous ?", ["scatter", "line", "bar", "pie"])

# Graphiques en fonction de la sélection
if x_col and y_col:
    if chart_type == "scatter":
        st.write("### Graphique SCATTER")
        fig, ax = plt.subplots()  # Create figure and axes
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)  # Pass the figure to st.pyplot()

    elif chart_type == "line":
        st.write("### Graphique LINE")
        fig, ax = plt.subplots()  # Create figure and axes
        sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)  # Pass the figure to st.pyplot()

    elif chart_type == "bar":
        st.write("### Graphique BAR")
        fig, ax = plt.subplots()  # Create figure and axes
        sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)  # Pass the figure to st.pyplot()

    elif chart_type == "pie":
        if df[y_col].dtype == "object" or df[y_col].dtype.name == "category":
            st.write("### Graphique PIE")
            fig, ax = plt.subplots()  # Create figure and axes
            pie_data = df[y_col].value_counts()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # For a perfect circle
            st.pyplot(fig)  # Pass the figure to st.pyplot()
        else:
            st.write("Sélectionnez une colonne catégorielle pour le graphique en camembert.")

# Corrélation
if st.checkbox("Afficher la matrice de corrélation"):
    st.write("### Matrice de Corrélation")
    corr = df.select_dtypes(include="number").corr()
    fig, ax = plt.subplots()  # Create figure and axes
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)  # Pass the figure to st.pyplot()