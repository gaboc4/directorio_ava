import os
import pandas as pd
import argparse


def create_statements(fpath):
	businesses = pd.read_csv(os.path.join(fpath))
	user_id = 1

	for _, row in businesses.iterrows():
		user_id += 1
		print('INSERT INTO business VALUES ("%s", %s, "%s", "%s", "%s", "%s", "%s")' %
		      (row['Nombre de Compañia '], user_id, row['Email'], row['Número de Teléfono'], 'Sector', row['Dirección'],
		       row['Descripcion de Servicio']))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('--path')
	businesses_path = parser.parse_args()

	create_statements(businesses_path.path)
