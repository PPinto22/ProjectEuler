comb = 0

for eur2 in range(0,2):
	_sum = 200*eur2
	if _sum == 200:
		comb += 1
	elif _sum < 200:
		for eur1 in range(0,3):
			_sum = 200*eur2 + 100*eur1
			if _sum == 200:
				comb += 1
			elif _sum < 200:
				for cent50 in range(0,5):
					_sum = 200*eur2 + 100*eur1 + 50*cent50
					if _sum == 200:
						comb += 1
					elif _sum < 200:
						for cent20 in range(0,11):
							_sum = 200*eur2 + 100*eur1 + 50*cent50 + 20*cent20
							if _sum == 200:
								comb += 1
							elif _sum < 200:
								for cent10 in range(0,21):
									_sum = 200*eur2 + 100*eur1 + 50*cent50 + 20*cent20 + 10*cent10
									if _sum == 200:
										comb += 1
									elif _sum < 200:
										for cent5 in range(0,41):
											_sum = 200*eur2 + 100*eur1 + 50*cent50 + 20*cent20 + 10*cent10 + 5*cent5
											if _sum == 200:
												comb += 1
											elif _sum < 200:
												for cent2 in range(0,101):
													_sum = 200*eur2 + 100*eur1 + 50*cent50 + 20*cent20 + 10*cent10 + 5*cent5 + 2*cent2											
													if _sum == 200:
														comb += 1
													elif _sum < 200:
														for cent1 in range(0,201):
															_sum = 200*eur2 + 100*eur1 + 50*cent50 + 20*cent20 + 10*cent10 + 5*cent5 + 2*cent2 + cent1													
															if _sum == 200:
																comb += 1

print(comb)