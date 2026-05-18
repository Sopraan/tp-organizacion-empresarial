
import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_csv('../datos/ventas.csv')

ventas_totales = ventas['precio'].sum()

producto_mas_vendido = ventas.groupby('producto')['cantidad'].sum().idxmax()

ventas['fecha'] = pd.to_datetime(ventas['fecha'])

ventas['mes'] = ventas['fecha'].dt.month

ventas_por_mes = ventas.groupby('mes')['precio'].sum()

print('Ventas totales:', ventas_totales)
print('Producto más vendido:', producto_mas_vendido)

resumen = pd.DataFrame({
    'ventas_totales': [ventas_totales],
    'producto_mas_vendido': [producto_mas_vendido]
})

resumen.to_csv('../resultados/resumen_ventas.csv', index=False)

ventas_por_mes.plot(kind='bar')

plt.title('Ventas por Mes')

plt.xlabel('Mes')

plt.ylabel('Ventas')

plt.savefig('../resultados/grafico_ventas.png')
