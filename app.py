import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("RandomForest.pkl", "rb"))

def type_res(types1):
	dic = {
		"Bug": 0,
		"Dark": 1,
		"Dragon": 2,
		"Electric": 3,
		"Fairy": 4,
		"Fighting": 5,
		"Fire": 6,
		"Flying": 7,
		"Ghost": 8,
		"Grass": 9,
		"Ground": 10,
		"Ice": 11,
		"Normal": 12,
		"Poison": 13,
		"Psychic": 14,
		"Rock": 15,
		"Steel": 16,
		"Water": 17
	}

	return dic.get(types1)

types1 = ["Water", "Normal", "Grass", "Bug", "Psychic", "Fire", "Electric", "Rock",
	  "Dragon", "Ghost", "Dark", "Poison", "Steel", "Fighting", "Ice", "Fairy", "Flying"]



names = st.text_input("Name")
type1 = st.selectbox("Type", types1)
total = st.number_input("Total")
hp = st.number_input("HP")
attack = st.number_input("Attack")
defense = st.number_input("Defense")
spec_atk = st.number_input("Special Attack")
spec_def = st.number_input("Special Defense")
speed = st.number_input("Speed")
generation = st.number_input("Generation")

if st.button("Find"):
	type1 = type_res(type1)
	test = np.array([[type1, total, hp, attack, defense, spec_atk, spec_def, speed, generation]])
	res = model.predict(test).item()
	if res == 0:
		st.warning("Not Legendary !")
	else:
		st.success("Legendary !")
