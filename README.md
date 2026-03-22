# Computational-Drug-Design-QSAR-codes
# Applicablity domain.
In QSAR modeling, the (AD) is the hypothetical space in a chemical border that encompasses the molecular characteristics and structural properties of the compounds utilized to develop the model of QSAR. This domain serves as a critical boundary for ensuring that the model's predictions remain reliable and valid within the defined chemical space.To assess the AD, William's plot was utilized, which maps consistent residuals beside the leverage values (h) of the compounds. The leverage value quantifies how far a compound's descriptor profile deviates from the center of the training data set. A compound is considered to be within the applicability domain if its leverage value is below the critical threshold (h*), and its standardized residual lies within ±3. Compounds falling outside this region are flagged as outliers, suggesting unreliable predictions for those molecules.
# William's plot 
William's plot was generated using Matplotlib v3.10.1, a widely used open-source Python library for creating static, animated, and interactive visualizations. This visualization effectively identifies influential molecules and defines the model's predictive boundary.
This method effectively identifies influential molecules and defines the model’s predictive boundary. The term outlier is used for any molecule whose descriptor values or biological response deviate significantly from the trained chemical space. If the cross-validated standardized residual of a compound exceeds ±3, it is also considered an outlier, even if its leverage is within acceptable limits

The warning leverage value (h*) is calculated using the following equation:

h^*=  3(p+1))/n
Where:

•	h* = Threshold leverage value

•	p = Numeral quantity of molecular descriptors used

•	n = Number of the compounds in training data

This leverage-based approach delivers a robust framework for studying the model's applicability domain and ensures that the predictions are confined to a chemically and statistically valid space.

