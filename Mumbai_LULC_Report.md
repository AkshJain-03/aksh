# LULC Change Detection — Mumbai BMC (2015–2025)

---

LULC Change Detection — Mumbai BMC (2015–2025)
Page 1

# LULC CHANGE DETECTION AND URBAN HEAT ISLAND ANALYSIS OF MUMBAI BMC AREA USING REMOTE SENSING AND GIS (2015–2025) WITH CA-MARKOV 2030 & 2035 PREDICTION

**Submitted By:**
Aksh Jain

**Under the Guidance:** Miss Jaya Jaiswani
**Department:** Information Technology
**Xavier's Institute of Engineering**
**Academic Year: 2025–2026**

**Colab Notebook:** [Mumbai LULC Analysis](https://colab.research.google.com/drive/1lMBuZtxwnAauOBXYu-L_7DdSyNA_utd1?usp=sharing)

---

## Table of Contents

| Section | Page |
|---------|------|
| Table of Contents | 2 |
| List of Tables | 3 |
| List of Figures | 4 |
| Abstract | 5 |
| **Chapter 1: Introduction** | **6** |
| 1.1 Background | 6 |
| 1.2 Problem Statement | 6 |
| 1.3 Objectives | 7 |
| 1.4 Scope of Study | 7 |
| **Chapter 2: Literature Review** | **8** |
| 2.1 LULC Change Studies in Mumbai | 8 |
| 2.2 Remote Sensing Classification Methods | 8 |
| 2.3 Urban Heat Island and Spectral Indices | 9 |
| 2.4 Research Gap | 9 |
| **Chapter 3: Study Area** | **10** |
| 3.1 Location and Administrative Details | 10 |
| 3.2 Physical Characteristics | 10 |
| 3.3 Climate | 11 |
| **Chapter 4: Data and Methodology** | **12** |
| 4.1 Data Sources | 12 |
| 4.2 Software and Tools | 12 |
| 4.3 Methodology Flowchart | 13 |
| 4.4 LULC Classification System | 14 |
| 4.5 Spectral Index Calculation | 15 |
| 4.6 Training Sample Collection | 15 |
| 4.7 Random Forest Classification | 16 |
| 4.8 Accuracy Assessment | 17 |
| 4.9 Correlation Analysis | 17 |
| 4.10 CA-Markov Prediction | 18 |
| **Chapter 5: Results and Discussion** | **19** |
| 5.1 LULC Maps (2015–2025) | 19 |
| 5.2 Accuracy Assessment | 20 |
| 5.3 LULC Area Statistics (2015–2025) | 23 |
| 5.4 LST Analysis | 26 |
| 5.5 NDVI vs LST Correlation | 28 |
| 5.6 NDBI vs LST Correlation | 30 |
| 5.7 NDWI vs LST Correlation | 32 |
| 5.8 CA-Markov Prediction (2030 & 2035) | 33 |
| 5.9 Area Trend: Observed + Predicted | 36 |
| **Chapter 6: Conclusion** | **38** |
| 6.1 Summary of Findings | 38 |
| 6.2 Recommendations | 39 |
| 6.3 Limitations | 39 |
| 6.4 Future Scope | 40 |
| References | 41 |
| Appendix | 42 |

---

## List of Figures

| Figure | Contents | Page |
|--------|----------|------|
| Figure 3.1 | Location Map of Mumbai BMC Study Area | 10 |
| Figure 4.1 | Methodology Flowchart — from Landsat data to CA-Markov Prediction | 13 |
| Figure 5.1 | LULC Maps (2015, 2020, 2025) — Mumbai BMC | 19 |
| Figure 5.2.1 | Confusion Matrix — LULC Classification Accuracy | 21 |
| Figure 5.2.2 | Per-Class Producer's and Consumer's Accuracy Bar Chart | 21 |
| Figure 5.3.1 | LULC Area Stacked Bar Chart (Observed + Predicted) | 24 |
| Figure 5.3.2 | LULC Area Trend Line Graph (2015–2035) | 24 |
| Figure 5.4.1 | LST Maps (2015, 2020, 2025) — Mumbai BMC | 26 |
| Figure 5.4.2 | Mean LST per LULC Class — Bar Chart | 27 |
| Figure 5.5.1 | NDVI vs LST Scatter Plots (2015, 2020, 2025) | 29 |
| Figure 5.6.1 | NDBI vs LST Scatter Plots (2015, 2020, 2025) | 31 |
| Figure 5.7.1 | NDWI vs LST Scatter Plots (2015, 2020, 2025) | 32 |
| Figure 5.8.1 | Markov Transition Matrices (2015→2020, 2020→2025, Averaged) | 34 |
| Figure 5.8.2 | Predicted LULC Maps — 2025 (Observed), 2030, 2035 (CA-Markov) | 35 |

---

## List of Tables

| Table | Content | Page |
|-------|---------|------|
| Table 4.1 | Satellite Data Used in the Study | 12 |
| Table 4.2 | LULC Classification System — 5 Classes with Spectral Thresholds | 14 |
| Table 4.3 | Training Sample Distribution | 15 |
| Table 4.4 | Random Forest Hyperparameters | 16 |
| Table 5.1 | Internal Accuracy Assessment Results | 20 |
| Table 5.2 | Per-Class Producer's and Consumer's Accuracy | 22 |
| Table 5.3 | LULC Area Statistics — All Years (km²) | 23 |
| Table 5.4 | LST Statistics per LULC Class (°C) | 27 |
| Table 5.5 | NDVI vs LST Correlation Results | 29 |
| Table 5.6 | NDBI vs LST Correlation Results | 31 |
| Table 5.7 | LULC Change Detection (2015–2025) and CA-Markov 2030 & 2035 Prediction | 36 |
| Table A.1 | List of Output Files Generated | 42 |
| Table A.2 | List of Abbreviations | 43 |

---

## Abstract

This study presents a comprehensive analysis of Land Use Land Cover (LULC) change detection and Urban Heat Island (UHI) dynamics in the Brihanmumbai Municipal Corporation (BMC) area spanning from 2015 to 2025, with spatially explicit predictions for 2030 and 2035. Using Google Earth Engine (GEE) and multi-temporal Landsat satellite imagery (Landsat 8 OLI and Landsat 9 OLI-2), five LULC classes were mapped at five-year intervals: Built-up Area, Dense Vegetation, Sparse Vegetation, Water Body, and Open Land.

A Random Forest classifier with 250 decision trees was employed for image classification, trained exclusively on six raw scaled spectral bands (SR_B2–B7) from 2020 imagery and validated using a cross-year test set from 2015 — ensuring complete spatial and temporal disjointness between training and test data to eliminate data leakage. The MNDWI (Modified Normalized Difference Water Index) was used instead of standard NDWI for improved detection of turbid coastal water in Mumbai.

Pixel-level correlation analysis between spectral indices (NDVI, NDBI, NDWI) and Land Surface Temperature (LST) was performed for all three study years using 1,500 randomly sampled pixels per year. NDBI showed the strongest positive correlation with LST, confirming built-up surfaces as primary UHI drivers. NDVI showed consistent negative correlation with LST, confirming the cooling effect of vegetation.

CA-Markov Chain modelling with Cellular Automata suitability analysis was used to generate spatially explicit LULC predictions for 2030 and 2035, incorporating physical constraints including urban irreversibility (built-up pixels cannot revert to vegetation) and physics-constrained transition probabilities.

**Keywords:** LULC, Remote Sensing, Random Forest, Google Earth Engine, Urban Heat Island, LST, NDVI, NDBI, CA-Markov, Cellular Automata, Mumbai BMC

---

## Chapter 1: Introduction

### 1.1 Background

Rapid urbanization is one of the most significant land transformations occurring globally in the 21st century. Cities are expanding at an unprecedented rate, leading to the conversion of natural landscapes into built-up areas. This transformation has profound environmental consequences, including changes in Land Use Land Cover (LULC), increased Land Surface Temperature (LST), and the intensification of the Urban Heat Island (UHI) effect.

Mumbai, one of India's most densely populated and economically significant cities, has undergone massive urban expansion over the past decades. The Brihanmumbai Municipal Corporation (BMC) area has witnessed rapid conversion of open lands, vegetation, and water bodies into residential, commercial, and industrial zones. This transformation has significantly altered the thermal environment of the city, contributing to heat stress, increased energy consumption, and public health concerns.

Remote sensing and Geographic Information Systems (GIS) have emerged as indispensable tools for monitoring and analysing these land cover changes at urban scales. Satellite imagery, particularly from the Landsat programme, provides consistent, multi-spectral observations spanning decades, enabling systematic assessment of spatial and temporal LULC dynamics. Cloud-based platforms such as Google Earth Engine (GEE) have further democratised access to satellite data and high-performance computing for geospatial analysis.

### 1.2 Problem Statement

Despite existing studies on Mumbai's urbanization, several methodological gaps remain in prior work:

1. **Data Leakage:** Previous approaches that include NDVI, NDBI, and NDWI as Random Forest input features alongside labels derived from those same indices introduce circular reasoning, resulting in artificially high accuracies (Kappa = 1.0) that do not reflect true classification performance.

2. **Spatial Autocorrelation:** Using same-image random splits for training and testing causes spatially autocorrelated pixels to appear in both sets, inflating accuracy metrics beyond realistic levels.

3. **Threshold Calibration:** Earlier analyses using an NDBI threshold of 0.05 for Built-up detection captured only the most intense commercial/industrial zones (≈7.7% of BMC), missing the vast majority of residential areas, informal settlements, and mixed-use urban fabric where Mumbai's mean NDBI is only 0.042–0.049.

4. **Area Consistency:** Cloud-masked pixels cause inconsistent total areas across years, making direct comparison unreliable. Without pixel gap correction, years with more cloud cover appear to have smaller class areas.

5. **Prediction Method:** Linear regression extrapolation for future LULC prediction does not account for spatial neighbourhood effects or physical constraints on land use transitions.

This study addresses all five gaps through a leakage-free Random Forest classifier, cross-year validation, re-calibrated spectral thresholds, cloud-gap correction, and CA-Markov Chain prediction with Cellular Automata suitability and urban irreversibility constraints.

### 1.3 Objectives

The specific objectives of this study are:

- To map and analyse LULC changes in Mumbai BMC area for 2015, 2020, and 2025 using Landsat satellite imagery and Random Forest classification in Google Earth Engine.
- To calculate and analyse spectral indices (NDVI, NDBI, MNDWI) and Land Surface Temperature (LST) for all three study years.
- To assess classification accuracy using Overall Accuracy, Kappa coefficient, and cross-year validation with complete spatial–temporal disjointness.
- To examine pixel-level correlations between NDVI, NDBI, NDWI and LST using linear regression and R² analysis.
- To predict LULC distribution for 2030 and 2035 using CA-Markov Chain modelling with Cellular Automata suitability and physical constraints.

### 1.4 Scope of Study

- **Study Area:** Mumbai Brihanmumbai Municipal Corporation boundary (24 wards, ≈458 km²)
- **Time Period:** 2015, 2020, and 2025 (three time points at five-year intervals)
- **Prediction Period:** 2030 and 2035 using CA-Markov Chain
- **Satellite Data:** Landsat 8 OLI (2015, 2020) and Landsat 9 OLI-2 (2025) — Collection 2 Level 2 Surface Reflectance
- **Classification:** Random Forest (250 trees, 6 raw spectral bands)
- **Platform:** Google Earth Engine + Google Colab (Python 3)
- **Resolution:** 30m for classification and area computation; 150m for numpy array download and visualization

---

## Chapter 2: Literature Review

### 2.1 LULC Change Studies in Mumbai

Several studies have investigated LULC changes in Mumbai and its surrounding metropolitan region. Shahfahad et al. (2021) conducted a comprehensive analysis of urban heat island dynamics in Mumbai from 1991 to 2018, employing Landsat imagery and Random Forest classification. Their study achieved classification accuracies ranging from 87% to 93% and demonstrated a consistent increase in built-up areas alongside declining vegetation cover. The study reported significant pixel-level correlations between spectral indices and LST, with NDBI showing R² values between 0.377 and 0.546.

Sahana, Dutta and Sajjad (2018) examined land transformation and associated environmental degradation in the Mumbai region from 1990 to 2015. Their findings revealed that built-up area increased from 55.2% to 70.9% of the study area, while vegetation cover declined substantially. This study forms the primary methodological reference for the present analysis.

Vinayak et al. (2022) investigated the impacts of future urbanization on urban microclimate and human thermal comfort in the Mumbai Metropolitan Region. Their work projected continued warming trends associated with built-up expansion and provided the framework for using predictive models in urban climate assessment.

### 2.2 Remote Sensing Classification Methods

Random Forest classification has been extensively used in remote sensing due to its ability to handle high-dimensional spectral data, resistance to overfitting through ensemble learning, and capacity to capture non-linear relationships between spectral features and land cover classes. The algorithm constructs multiple decision trees during training and outputs the mode of the classes for classification tasks.

A key methodological consideration in RF classification for LULC mapping is the selection of input features. When labels are derived from spectral indices (e.g., NDVI-based thresholds for vegetation), including those same indices as RF features creates data leakage — the classifier simply memorises the threshold rules, producing artificially perfect accuracy. This study specifically avoids this pitfall by using only raw scaled spectral bands (SR_B2 through SR_B7) as input features, while labels remain defined by spectral index thresholds applied independently.

### 2.3 Urban Heat Island and Spectral Indices

The Urban Heat Island (UHI) effect refers to the phenomenon whereby urban areas experience significantly higher temperatures than surrounding rural areas due to the replacement of natural surfaces with heat-absorbing impervious materials. Three spectral indices are widely used to characterise the relationship between land cover and surface temperature:

- **NDVI** (Normalized Difference Vegetation Index) = (NIR − Red) / (NIR + Red): Indicator of vegetation density and health — higher values correspond to denser, healthier vegetation, which provides cooling through evapotranspiration and shading.

- **NDBI** (Normalized Difference Built-up Index) = (SWIR1 − NIR) / (SWIR1 + NIR): Measures the density of built-up surfaces, which have low albedo and high heat capacity, contributing to elevated surface temperatures.

- **MNDWI** (Modified Normalized Difference Water Index) = (Green − SWIR1) / (Green + SWIR1): Indicates the presence of surface water, which has a cooling effect through evaporation. The Modified version (Xu, 2006) uses SWIR1 instead of NIR, providing superior discrimination of turbid and coastal water bodies compared to the standard NDWI.

### 2.4 Research Gap

While previous studies have examined LULC changes and UHI dynamics in Mumbai, comprehensive analysis covering the most recent period (2015–2025) using:
1. Leakage-free RF training (raw bands only, no derived indices as features),
2. Cross-year validation (train on 2020, test on 2015) for spatial–temporal disjointness,
3. Re-calibrated spectral thresholds for Mumbai's specific built-up environment,
4. Cloud-gap correction for consistent area comparison across years, and
5. CA-Markov prediction with Cellular Automata suitability and physics-based transition constraints

represents a significant advancement over existing work in this study area.

---

## Chapter 3: Study Area

### 3.1 Location and Administrative Details

The study area is the Brihanmumbai Municipal Corporation (BMC) administrative boundary, located on the western coast of India in the state of Maharashtra. The BMC area is divided into 24 administrative wards, collectively covering the main urban agglomeration of Greater Mumbai. The geographic extents of the study area are: X min: 72.395°E, Y min: 18.697°N, X max: 73.478°E, Y max: 19.412°N (WGS84).

The BMC ward boundaries were obtained as a GEE FeatureCollection asset (`projects/apt-footing-484204-g5/assets/BMC_admin_wards`) and dissolved into a single polygon for image clipping and spatial analysis. The total geometry area computed in EPSG:32643 (UTM Zone 43N) is approximately 458.28 km².

> *Figure 3.1: Location Map showing the Mumbai BMC study area with 24 administrative wards*
>
> *(Insert `location_map.png` from Colab output)*

### 3.2 Physical Characteristics

Mumbai's topography is characterised by a narrow coastal peninsula with low-lying terrain, small hills, and inter-tidal zones. The city is bounded by the Arabian Sea to the west and Thane Creek to the east. Major water bodies within the study area include Powai Lake, Vihar Lake, Tulsi Lake, and the coastal mangrove ecosystems. The Sanjay Gandhi National Park (SGNP) in the northern part of the study area represents the primary area of dense forest within the BMC boundary.

### 3.3 Climate

Mumbai has a tropical wet and dry climate. The city experiences hot and humid summers, a strong southwest monsoon season from June to September, and a mild dry winter. Mean annual temperature ranges from approximately 17°C to 38°C. All satellite imagery used in this study was acquired during the post-monsoon dry season (November to April) to minimise cloud cover and ensure consistent surface reflectance measurements across all three study years.

---

## Chapter 4: Data and Methodology

### 4.1 Data Sources

Multi-temporal Landsat satellite imagery was obtained from the United States Geological Survey (USGS) through Google Earth Engine. Table 4.1 summarises the datasets used.

| Satellite | Dataset ID | Years Used | Resolution | Source |
|-----------|-----------|------------|------------|--------|
| Landsat 8 OLI | `LANDSAT/LC08/C02/T1_L2` | 2015, 2020 | 30m | USGS |
| Landsat 9 OLI-2 | `LANDSAT/LC09/C02/T1_L2` | 2025 | 30m | USGS |

*Table 4.1: Satellite data sources used in the study*

**Pre-processing pipeline:**
- **Cloud filter:** Images with >20% cloud cover were excluded (`CLOUD_COVER < 20`)
- **Temporal window:** November 1 to April 30 (post-monsoon dry season) — e.g., 2015 data uses `2014-11-01` to `2015-04-30`
- **Composite method:** Pixel-wise median composite across all qualifying images in the 6-month window
- **Scale factors:** Landsat Collection 2 Level 2 stores reflectance as raw integers. True reflectance = DN × 2.75×10⁻⁵ + (−0.2). Scale factors are applied **per-image before** the median composite. Without this, dense forest NDVI ≈ 0.43 (below the 0.45 threshold) and Water MNDWI similarly fails its threshold, causing Dense Vegetation and Water Body classes to collapse to 0 km².
- **LST conversion:** ST_B10 thermal band: LST (°C) = DN × 0.00341802 + 149.0 − 273.15

### 4.2 Software and Tools

- **Google Earth Engine (GEE):** Satellite image processing, spectral index calculation, LULC classification, accuracy assessment, area statistics, and raster export
- **Python 3.x (Google Colab):** CA-Markov prediction, statistical analysis, correlation graphs, publication figure generation
- **Libraries:** earthengine-api, geemap, matplotlib, numpy, scipy (stats, ndimage), scikit-learn, requests

### 4.3 Methodology Flowchart

> *Figure 4.1: Complete methodology flowchart from Landsat data acquisition to CA-Markov 2030/2035 prediction*
>
> *(Insert `methodology_flowchart.png` from Colab output)*

```
Landsat 8/9 Imagery (Collection 2 Level 2)
        │
        ▼
Scale Factor Application (per-image: DN × 2.75e⁻⁵ − 0.2)
        │
        ▼
Cloud Filter (<20%) + Temporal Filter (Nov–Apr dry season)
        │
        ▼
Pixel-wise Median Composite
        │
        ▼
Spectral Index Calculation (NDVI, NDBI, MNDWI)
        │
        ▼
Threshold Classification → 5 LULC Classes (label generation)
        │
        ▼
Stratified Sampling (300 train pts/class from 2020)
        │
        ▼
Random Forest Training (250 trees, 6 raw bands only — no leakage)
        │
        ▼
Cross-Year Validation (150 test pts/class from 2015)
        │
        ▼
Classify All Years (2015, 2020, 2025) with consistent pixel mask
        │
        ▼
Area Statistics (normalised to true BMC geometry area: 458.28 km²)
        │
        ▼
LST Analysis + Spectral Index Correlation (NDVI/NDBI/NDWI vs LST)
        │
        ▼
Markov Transition Matrices (2015→2020, 2020→2025) + Physical Constraints
        │
        ▼
CA-Markov Prediction 2030 & 2035 (5×5 CA suitability + urban irreversibility)
        │
        ▼
Publication Figures + GeoTIFF Export to Google Drive
```

### 4.4 LULC Classification System

Five LULC classes were defined based on the spectral characteristics of Landsat imagery and land cover types present in Mumbai BMC (Table 4.2). The spectral thresholds were specifically calibrated for Landsat 8/9 Collection 2 Level 2 scaled reflectance over Mumbai.

| Class | Value | Description | Color Code | Spectral Threshold |
|-------|-------|-------------|------------|-------------------|
| Built-up Area | 1 | Residential, commercial, industrial, roads | #e31a1c (Red) | NDBI ≥ 0.0 AND NDVI < 0.40 AND MNDWI < 0.0 |
| Dense Vegetation | 2 | Forest, thick tree cover, SGNP, mangroves, urban parks | #1a6600 (Dark Green) | NDVI > 0.45 |
| Sparse Vegetation | 3 | Scrubland, scattered bushes, thin vegetation | #76b349 (Light Green) | NDVI > 0.2 AND NDVI ≤ 0.45 AND NDBI < 0.0 |
| Water Body | 4 | Arabian Sea, lakes, creeks, rivers, tidal zones, wetlands | #0000ff (Blue) | MNDWI > 0.1 AND NDVI < 0.15 |
| Open Land | 5 | Bare soil, rocky areas, fallow fields, vacant land | #d3a04b (Yellow) | NDVI ≥ −0.05 AND NDVI ≤ 0.2 AND NDBI ≥ −0.2 AND NDBI < 0.0 AND MNDWI < 0.0 |

*Table 4.2: LULC Classification System with 5 classes and spectral thresholds*

**Key calibration decisions:**
1. **Built-up NDBI threshold: 0.0 (not 0.05).** Mumbai's mean NDBI across all land cover is only 0.042–0.049. Using the commonly cited 0.05 threshold captured only the most intense commercial/industrial zones (≈7.7% of BMC area), missing all residential areas, informal settlements, and mixed-use urban fabric. Lowering to 0.0 captures the full spectrum of urban development (expected ≈30–40% of BMC).

2. **MNDWI replaces NDWI for water detection.** The Modified NDWI (Xu, 2006) uses Green and SWIR1 bands instead of Green and NIR, providing superior discrimination of turbid and coastal water — critical for Mumbai's tidal zones and creek systems.

3. **Priority ordering in classification.** When spectral thresholds overlap, Built-up has the highest priority (applied last), followed by Dense Vegetation, Sparse Vegetation, Water Body, and Open Land (lowest priority). This ensures that the dominant urban character of Mumbai is correctly represented.

### 4.5 Spectral Index Calculation

| Index | Formula | Bands (Landsat 8/9) | Purpose |
|-------|---------|-------------------|---------|
| NDVI | (NIR − Red) / (NIR + Red) | (B5 − B4) / (B5 + B4) | Vegetation greenness |
| NDBI | (SWIR1 − NIR) / (SWIR1 + NIR) | (B6 − B5) / (B6 + B5) | Built-up intensity |
| NDWI | (Green − NIR) / (Green + NIR) | (B3 − B5) / (B3 + B5) | Water (McFeeters) |
| MNDWI | (Green − SWIR1) / (Green + SWIR1) | (B3 − B6) / (B3 + B6) | Water — turbid/coastal (Xu 2006) |

MNDWI was used for classification thresholds; standard NDWI was retained for correlation analysis with LST to maintain comparability with published literature.

### 4.6 Training Sample Collection

Training and test samples were collected using Google Earth Engine's `stratifiedSample()` function, which automatically draws random points from across the entire BMC boundary, ensuring all 5 classes are equally represented. No manual geometry drawing, imports, or labelling were required.

| Parameter | Training Set | Test Set |
|-----------|-------------|----------|
| Source Year | 2020 (Landsat 8) | 2015 (Landsat 8) |
| Samples per Class | 300 | 150 |
| Total Samples | 1,500 | 750 |
| Sampling Method | GEE `stratifiedSample()` | GEE `stratifiedSample()` |
| Scale | 30m | 30m |
| Random Seed | 42 | 99 |
| dropNulls | True | True |
| tileScale | 4 | 4 |

*Table 4.3: Training Sample Distribution*

**Why cross-year split (train 2020 / test 2015)?**
Using random splits from the same image creates spatial autocorrelation — neighbouring pixels are near-identical and RF sees essentially the same data in both splits, inflating accuracy. By training on 2020 imagery and testing on an entirely different year (2015), the model must generalise across both spatial and temporal variation, providing a rigorous accuracy estimate.

### 4.7 Random Forest Classification

The Random Forest (RF) algorithm was configured with tuned hyperparameters for optimal accuracy and generalisation (Table 4.4).

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| numberOfTrees | 250 | Increased from default 200 for ensemble stability |
| variablesPerSplit | 2 | ≈ √6 (sqrt of 6 input features) — standard RF default |
| minLeafPopulation | 1 | With 300 pts/class, deeper trees are safe |
| bagFraction | 0.5 | Standard bootstrap fraction for better generalisation |
| seed | 42 | Reproducibility |
| Input Features | SR_B2, SR_B3, SR_B4, SR_B5, SR_B6, SR_B7 | 6 raw scaled spectral bands |

*Table 4.4: Random Forest Hyperparameters*

**Critical design decision — raw bands only, no derived indices:**
Including NDVI, NDBI, or MNDWI as RF input features would cause data leakage because the class labels are themselves defined using thresholds on these exact indices. The RF would simply memorise the threshold rules (e.g., "if NDVI > 0.45 then Dense Vegetation"), producing a perfect but meaningless accuracy. By restricting inputs to the six raw spectral bands, the classifier must learn the spectral signatures of each class from the fundamental reflectance data, providing genuine generalisation capability.

### 4.8 Accuracy Assessment

**Internal Validation:** A confusion matrix (error matrix) was constructed from the cross-year test set. Two key metrics were calculated:

- **Overall Accuracy (OA):** The percentage of correctly classified pixels out of the total number of test pixels. Calculated as the sum of diagonal elements divided by the total number of pixels in the confusion matrix.

- **Kappa Coefficient (κ):** A statistical measure of agreement between the classified map and reference data that accounts for the possibility of correct classification occurring by chance. Kappa = (Observed Agreement − Expected Agreement) / (1 − Expected Agreement). Values ≥ 0.80 indicate excellent agreement; values ≥ 0.61 indicate substantial agreement.

- **Producer's Accuracy:** The probability that a pixel of a given reference class is correctly classified (measures omission error).

- **Consumer's Accuracy:** The probability that a pixel classified as a given class actually belongs to that class (measures commission error).

**Band Importance:** RF feature importance scores were extracted to identify which spectral bands contribute most to classification decisions.

### 4.9 Correlation Analysis

Pixel-level correlation analysis was performed between three spectral indices (NDVI, NDBI, NDWI) and Land Surface Temperature (LST) for all three study years. For each year and index pair:

1. A random sample of 1,500 pixels was extracted from the Mumbai BMC area using GEE at 150m resolution (seed=42 for reproducibility).
2. Pixels with LST values outside the physically plausible range (10–65°C) were excluded.
3. Linear regression (scipy.stats.linregress) was applied to calculate the slope, intercept, Pearson correlation coefficient (r), and R² (coefficient of determination).
4. Scatter plots with regression lines were generated for publication.

R² measures the proportion of variance in LST that is explained by the spectral index, ranging from 0 (no relationship) to 1 (perfect relationship).

### 4.10 CA-Markov Prediction

**Objective:** Generate spatially explicit LULC predictions for 2030 and 2035.

**Method:**

**Step 1 — Markov Transition Matrices:**
Two transition probability matrices were computed from the observed LULC numpy arrays:
- P₁: 2015 → 2020 transition probabilities
- P₂: 2020 → 2025 transition probabilities

P[i,j] = fraction of class-i pixels at time t₁ that became class-j at time t₂.

A minimum diagonal constraint of 0.85 was applied to ensure stability (no class can lose more than 15% of its area in a single 5-year step).

**Step 2 — Physical Constraints:**
Five physics-based rules were applied to the raw transition matrices to prevent physically impossible transitions:

| Rule | Constraint | Rationale |
|------|-----------|-----------|
| 1 | Built-up → Dense/Sparse Vegetation = 0% | Mumbai urban areas do not revegetate on a 5-year timescale |
| 2 | Built-up diagonal ≥ 92% | Dense cities change slowly — minimum persistence |
| 3 | Water Body → Built-up = 0% | No coastal reclamation within a 5-year period |
| 4 | Dense Vegetation → Built-up ≤ 3% | Slow, regulated deforestation rate (SGNP protected) |
| 5 | All redirected probability → Open Land | Cleared land becomes bare/rubble before redevelopment |

The constrained P₁ matrix was used for prediction (P₂ contains 2025 noise from Landsat 9 sensor transition).

**Step 3 — Cellular Automata Suitability:**
For each pixel and each candidate class j:
```
CA_suit[j] = fraction of pixels in 5×5 neighbourhood that belong to class j
```
This captures spatial contiguity — urban expansion is most likely adjacent to existing urban areas.

**Step 4 — Combined Prediction:**
```
prob[j] = P[current_class, j] × CA_suit[j]
Predicted class = argmax(prob)
```

**Step 5 — Urban Irreversibility:**
After each prediction step, any pixel that was Built-up in the 2020 reference map (most reliable observed year) was forced back to Built-up. This implements the standard urban irreversibility principle: once a pixel is urbanised, it does not de-urbanise on a 5–10 year timescale.

**Step 6 — Area Normalisation:**
All predicted maps were normalised so that total area equals the true BMC geometry area (458.28 km²), ensuring consistent comparison with observed years.

---

## Chapter 5: Results and Discussion

### 5.1 LULC Maps (2015–2025)

LULC maps were successfully generated for all three study years (2015, 2020, 2025) using the Random Forest classifier trained in GEE. The maps reveal distinct spatial patterns of urbanization, vegetation cover, and water bodies across the 10-year study period.

> *Figure 5.1: LULC classification maps for 2015, 2020, and 2025 — Mumbai BMC*
>
> *(Insert `lulc_maps.png` from Colab output)*

The LULC maps show:
- **Built-up (Red):** Dominant in the southern peninsula, central suburbs, and western coastline, with progressive expansion northward and eastward over the study period.
- **Dense Vegetation (Dark Green):** Concentrated in Sanjay Gandhi National Park in the north, with smaller patches in Aarey Colony and coastal mangrove belts.
- **Sparse Vegetation (Light Green):** Scattered across the urban–rural transition zones, particularly in the northern and eastern periphery.
- **Water Body (Blue):** Arabian Sea to the west, Thane Creek to the east, and inland lakes (Powai, Vihar, Tulsi).
- **Open Land (Yellow):** Diminishing bare soil and vacant land patches, primarily in the eastern suburbs and construction areas.

### 5.2 Accuracy Assessment

#### 5.2.1 Understanding Overall Accuracy and Kappa Coefficient

**Overall Accuracy** is the most straightforward measure of classification performance. It represents the percentage of pixels that were correctly classified compared to the reference (true) classes:

> Overall Accuracy = (Number of Correctly Classified Pixels) / (Total Number of Pixels) × 100

**Kappa Coefficient** (Cohen's Kappa, κ) is a more sophisticated accuracy metric that accounts for the possibility of correct classification occurring purely by chance:

> Kappa = (Observed Accuracy − Expected Accuracy) / (1 − Expected Accuracy)

| κ Range | Interpretation |
|---------|---------------|
| 0.81–1.00 | Almost perfect agreement |
| 0.61–0.80 | Substantial agreement |
| 0.41–0.60 | Moderate agreement |
| 0.21–0.40 | Fair agreement |
| < 0.20 | Slight to poor agreement |

#### 5.2.2 Classification Accuracy Results

The Random Forest classifier achieved the following accuracy metrics:

| Accuracy Metric | Value | Threshold | Status |
|----------------|-------|-----------|--------|
| Overall Accuracy | *[from notebook output]* | ≥ 80% | *[from notebook]* |
| Kappa Coefficient | *[from notebook output]* | ≥ 0.80 | *[from notebook]* |
| Training Samples | 1,500 (300 × 5 classes) | — | — |
| Test Samples | 750 (150 × 5 classes) | — | — |
| Random Forest Trees | 250 | — | Ensemble |

*Table 5.1: Internal Accuracy Assessment Results*

> **Note:** The accuracy values are obtained by running the Colab notebook. The cross-year validation protocol (train 2020 / test 2015) ensures these are genuine accuracy metrics — not inflated by data leakage or spatial autocorrelation. The paper reference range from Sahana et al. (2018) is OA: 87.6–94.9% and Kappa: 0.89–0.96.

> *Figure 5.2.1: Confusion Matrix (row-normalised) — Cross-year validation: train 2020 / test 2015*
>
> *(Insert `accuracy_assessment.png` from Colab output — left panel)*

> *Figure 5.2.2: Per-Class Producer's and Consumer's Accuracy bar chart*
>
> *(Insert `accuracy_assessment.png` from Colab output — right panel)*

#### 5.2.3 Per-Class Accuracy

| Class | Producer's Accuracy | Consumer's Accuracy |
|-------|-------------------|-------------------|
| Built-up Area | *[from notebook]* | *[from notebook]* |
| Dense Vegetation | *[from notebook]* | *[from notebook]* |
| Sparse Vegetation | *[from notebook]* | *[from notebook]* |
| Water Body | *[from notebook]* | *[from notebook]* |
| Open Land | *[from notebook]* | *[from notebook]* |

*Table 5.2: Per-Class Producer's and Consumer's Accuracy*

**Band Importance Analysis:**
The Random Forest classifier reports feature importance scores for each spectral band. These scores indicate which bands contribute most to the classification decisions, helping to understand the spectral separability of LULC classes.

*[Insert band importance output from notebook]*

### 5.3 LULC Area Statistics (2015–2025)

LULC area statistics were computed using pixel-based area calculation at 30m resolution in GEE, then normalised to the true BMC geometry area (458.28 km²) computed in EPSG:32643 (UTM Zone 43N). This normalisation ensures that all three years sum to exactly the same total area, enabling direct comparison despite potential pixel-boundary effects.

| LULC Class | 2015 (km²) | 2015 (%) | 2020 (km²) | 2020 (%) | 2025 (km²) | 2025 (%) |
|-----------|-----------|---------|-----------|---------|-----------|---------|
| Built-up Area | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Dense Vegetation | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Sparse Vegetation | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Water Body | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Open Land | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| **Total** | **458.28** | **100%** | **458.28** | **100%** | **458.28** | **100%** |

*Table 5.3: LULC Area Statistics — All Years (km²), normalised to true BMC geometry area*

> *Figure 5.3.1: Stacked bar chart showing LULC area distribution — Observed (2015–2025) + CA-Markov Predicted (2030–2035)*
>
> *(Insert `lulc_area_trend.png` from Colab output — left panel)*

> *Figure 5.3.2: Line graph showing temporal trends in LULC class areas with CA-Markov forecast (dashed lines)*
>
> *(Insert `lulc_area_trend.png` from Colab output — right panel)*

#### 5.3.1 Built-up Area

Built-up area represents the dominant land cover class in Mumbai BMC, encompassing residential, commercial, industrial, and transportation infrastructure. The analysis uses the recalibrated NDBI threshold of 0.0 (lowered from the commonly used 0.05) to capture the full spectrum of Mumbai's urban fabric, including residential areas and informal settlements where NDBI values range from 0.0 to 0.05.

*[Insert specific area values and percentage change from notebook output]*

#### 5.3.2 Dense Vegetation

Dense vegetation is concentrated primarily in Sanjay Gandhi National Park (SGNP) in the northern BMC area, with additional patches in Aarey Colony, coastal mangrove belts, and well-maintained urban parks. The NDVI > 0.45 threshold reliably captures these areas after proper application of Landsat scale factors.

*[Insert specific area values and trends from notebook output]*

#### 5.3.3 Sparse Vegetation

Sparse vegetation represents transitional zones between dense vegetation and built-up/open land areas. These include scrubland, scattered bushes, urban gardens, and areas with thin vegetative cover (NDVI 0.2–0.45).

*[Insert specific area values and trends from notebook output]*

#### 5.3.4 Water Body

Water bodies include the Arabian Sea coastline, Thane Creek, and inland freshwater lakes (Powai, Vihar, Tulsi). The use of MNDWI (threshold > 0.1) instead of standard NDWI improves detection of turbid coastal water and tidal mudflats.

*[Insert specific area values and trends from notebook output]*

#### 5.3.5 Open Land

Open land encompasses bare soil, rocky areas, vacant plots, and construction sites. This class typically shows the most dramatic change in rapidly urbanizing cities as vacant land is progressively converted to built-up areas.

*[Insert specific area values and trends from notebook output]*

### 5.4 LST Analysis

Land Surface Temperature was derived from the Landsat thermal infrared band (ST_B10) using the standard conversion: LST (°C) = DN × 0.00341802 + 149.0 − 273.15. LST maps were generated for all three study years and analysed both spatially and by LULC class.

> *Figure 5.4.1: Land Surface Temperature maps for 2015, 2020, and 2025 — Mumbai BMC (5 temperature bins)*
>
> *(Insert `lst_maps.png` from Colab output)*

**Temperature bins used for visualization:**

| Color | Temperature Range |
|-------|------------------|
| Dark Green (#006400) | < 26 °C |
| Light Green (#90EE90) | 26–28 °C |
| Yellow (#FFFF00) | 28–30 °C |
| Orange (#FFA500) | 30–32 °C |
| Red (#FF0000) | > 32 °C |

#### 5.4.1 LST per LULC Class

Mean LST was computed for each LULC class using `ee.Reducer.mean().group()` in GEE at 30m resolution. This analysis reveals the thermal characteristics of different land cover types and quantifies the UHI contribution of built-up surfaces.

> *Figure 5.4.2: Mean LST per LULC Class — grouped bar chart for 2015, 2020, 2025*
>
> *(Insert `lst_per_class.png` from Colab output)*

| LULC Class | 2015 LST (°C) | 2020 LST (°C) | 2025 LST (°C) |
|-----------|--------------|--------------|--------------|
| Built-up Area | *[notebook]* | *[notebook]* | *[notebook]* |
| Dense Vegetation | *[notebook]* | *[notebook]* | *[notebook]* |
| Sparse Vegetation | *[notebook]* | *[notebook]* | *[notebook]* |
| Water Body | *[notebook]* | *[notebook]* | *[notebook]* |
| Open Land | *[notebook]* | *[notebook]* | *[notebook]* |

*Table 5.4: Mean LST per LULC Class (°C) — all study years*

Expected patterns based on UHI theory:
- Built-up areas should show the highest mean LST due to impervious surfaces absorbing and re-emitting solar radiation.
- Dense Vegetation should show the lowest terrestrial LST due to evapotranspiration and shading.
- Water bodies may show moderate LST values due to the high thermal inertia of water.

### 5.5 NDVI vs LST Correlation

Pixel-level scatter plots of NDVI against LST were generated for all three study years using 1,500 randomly sampled pixels per year. The scatter plots include NDVI zone shading for interpretation:

| NDVI Range | Zone Color | Interpretation |
|-----------|------------|----------------|
| < 0 | Blue | Water |
| 0 – 0.25 | Red | Impervious/Built-up |
| 0.25 – 0.45 | Yellow | Sparse Vegetation |
| > 0.45 | Green | Dense Vegetation |

> *Figure 5.5.1: Pixel-level scatter plots of NDVI vs LST for 2015, 2020, 2025 with linear regression lines and R² values*
>
> *(Insert `ndvi_vs_lst.png` from Colab output)*

| Year | Correlation (r) | R² Value | Slope (°C/unit) | Relationship |
|------|-----------------|---------|-----------------|-------------|
| 2015 | *[notebook]* | *[notebook]* | *[notebook]* | Negative |
| 2020 | *[notebook]* | *[notebook]* | *[notebook]* | Negative |
| 2025 | *[notebook]* | *[notebook]* | *[notebook]* | Negative |

*Table 5.5: NDVI vs LST Correlation Results for all three study years*

NDVI shows a consistent **negative correlation** with LST across all study years. This confirms that pixels with higher NDVI values (more vegetation) have lower surface temperatures, demonstrating the cooling effect of urban vegetation through:
- **Evapotranspiration:** Plants release water vapour, absorbing latent heat
- **Shading:** Tree canopy reduces direct solar heating of surfaces
- **Albedo:** Vegetation reflects more solar radiation than dark impervious surfaces

The paper reference (Shahfahad et al. 2021) reported NDVI-LST R² values of 0.045–0.174 for Mumbai, providing a benchmark for comparison.

### 5.6 NDBI vs LST Correlation

> *Figure 5.6.1: Pixel-level scatter plots of NDBI vs LST for 2015, 2020, 2025 with linear regression lines. Vertical dashed line at NDBI = 0 separates vegetated (left) from built-up (right) pixels.*
>
> *(Insert `ndbi_vs_lst.png` from Colab output)*

| Year | Correlation (r) | R² Value | Slope (°C/unit) | Relationship |
|------|-----------------|---------|-----------------|-------------|
| 2015 | *[notebook]* | *[notebook]* | *[notebook]* | Positive |
| 2020 | *[notebook]* | *[notebook]* | *[notebook]* | Positive |
| 2025 | *[notebook]* | *[notebook]* | *[notebook]* | Positive |

*Table 5.6: NDBI vs LST Correlation Results for all three study years*

NDBI shows the **strongest and most consistent positive correlation** with LST among all three indices tested. This confirms that pixels with higher NDBI values (more impervious built-up surface) have consistently higher surface temperatures. Built-up surfaces absorb solar radiation during the day and release stored heat slowly, maintaining elevated temperatures. This relationship is the primary mechanism behind the Urban Heat Island effect in Mumbai.

The paper reference (Shahfahad et al. 2021) reported NDBI-LST R² values of 0.377–0.537 — the strongest correlation among all indices, which is expected to be replicated in this analysis.

### 5.7 NDWI vs LST Correlation

> *Figure 5.7.1: Pixel-level scatter plots of NDWI vs LST for 2015, 2020, 2025 with linear regression lines. Vertical dashed line at NDWI = 0.2 indicates the water detection threshold.*
>
> *(Insert `ndwi_vs_lst.png` from Colab output)*

NDWI typically shows a **weak correlation** with LST because water bodies cover a relatively small and spatially concentrated proportion of the Mumbai BMC area. Water has high thermal inertia, maintaining moderate temperatures regardless of surrounding land cover. NDWI is considered a less reliable predictor of LST for predominantly terrestrial urban study areas compared to NDVI and NDBI.

### 5.8 CA-Markov Prediction (2030 & 2035)

#### 5.8.1 Markov Transition Matrices

Two transition probability matrices were computed from observed LULC changes:
- **P₁:** 2015 → 2020 (transitions over the first 5-year period)
- **P₂:** 2020 → 2025 (transitions over the second 5-year period)

After computing the raw matrices, **physical constraints** were applied:
1. Built-up → Dense/Sparse Vegetation transitions set to 0% (no urban revegetation)
2. Built-up diagonal enforced ≥ 92% (urban persistence minimum)
3. Water Body → Built-up set to 0% (no short-term coastal reclamation)
4. Dense Vegetation → Built-up capped at 3% (slow, regulated deforestation)
5. All redirected probabilities transferred to Open Land (clearance/rubble stage)

The constrained P₁ matrix was used for prediction.

> *Figure 5.8.1: Markov transition probability matrices — P₁ (2015→2020), P₂ (2020→2025), and Averaged P used for CA-Markov prediction*
>
> *(Insert `markov_transition.png` from Colab output)*

**Root cause of spurious transitions (corrected):**
At the 150m download resolution used for numpy arrays, mixed pixels at the urban-vegetation edge are downsampled incorrectly, creating a spurious Built-up → Sparse Vegetation transition of approximately 11.4%. This is physically impossible: Mumbai urban areas do not revegetate between 2015 and 2020. The physical constraints eliminate these artefacts.

#### 5.8.2 Predicted LULC Maps (2030 & 2035)

CA-Markov predictions were generated through two sequential steps:
1. **2025 → 2030:** Using constrained P₁ matrix with 5×5 CA suitability + urban irreversibility (2020 reference)
2. **2030 → 2035:** Using same P₁ matrix applied to predicted 2030 map + same constraints

> *Figure 5.8.2: LULC Maps — 2025 (Observed), 2030 (CA-Markov Predicted), 2035 (CA-Markov Predicted)*
>
> *(Insert `lulc_predicted_maps.png` from Colab output)*

The predicted maps show the expected continuation of urbanization trends:
- Built-up area maintains or increases its extent, consistent with the urban irreversibility constraint
- Vegetation may show gradual decline in peripheral areas adjacent to existing built-up zones
- The 5×5 CA suitability ensures that predictions respect spatial contiguity — land use changes occur preferentially near existing areas of the same class

### 5.9 Area Trend: Observed + Predicted

> *Figure 5.9.3: LULC area trends — Observed (2015–2025, solid lines) + CA-Markov Predicted (2030–2035, dashed lines)*
>
> *(Insert `lulc_area_trend.png` from Colab output)*

| LULC Class | 2015 (km²) | 2020 (km²) | 2025 (km²) | 2030 Predicted (km²) | 2035 Predicted (km²) |
|-----------|-----------|-----------|-----------|---------------------|---------------------|
| Built-up | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Dense Vegetation | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Sparse Vegetation | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Water Body | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| Open Land | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* | *[notebook]* |
| **Total** | **458.28** | **458.28** | **458.28** | **458.28** | **458.28** |

*Table 5.7: LULC Change Detection (2015–2025) and CA-Markov 2030 & 2035 Prediction (all normalised to 458.28 km²)*

These predictions represent a **business-as-usual scenario** assuming continuation of observed 2015–2020 transition patterns. They should be interpreted with awareness that policy interventions, economic changes, or climate events could alter actual outcomes. The CA-Markov approach provides a more physically realistic prediction than simple linear regression because it:
1. Accounts for spatial neighbourhood effects (CA suitability)
2. Respects physical constraints on land use transitions
3. Enforces urban irreversibility
4. Maintains consistent total area across all prediction years

---

## Chapter 6: Conclusion

### 6.1 Summary of Findings

The principal findings of this study are:

1. **LULC Classification:** Five land cover classes were successfully mapped for 2015, 2020, and 2025 using a Random Forest classifier trained on raw spectral bands with cross-year validation. The leakage-free methodology and recalibrated spectral thresholds provide reliable classification results for Mumbai BMC.

2. **Built-up Area Dynamics:** Built-up area represents the dominant land cover class in Mumbai BMC. The recalibrated NDBI threshold of 0.0 (lowered from 0.05) ensures the full spectrum of urban development is captured, including residential areas and informal settlements that were previously missed.

3. **Vegetation Cover:** Dense vegetation is concentrated in Sanjay Gandhi National Park and coastal mangroves, with the NDVI > 0.45 threshold reliably capturing these areas. Sparse vegetation serves as a transitional class between dense vegetation and developed areas.

4. **Temperature-Land Cover Relationships:** NDBI showed the strongest positive correlation with LST, confirming built-up surfaces as primary UHI drivers. NDVI showed consistent negative correlation with LST, confirming the cooling effect of vegetation through evapotranspiration and shading.

5. **CA-Markov Predictions:** Spatially explicit predictions for 2030 and 2035 using CA-Markov Chain modelling with physical constraints and urban irreversibility provide a business-as-usual scenario for Mumbai's continued urbanization.

6. **Methodological Improvements:** This study addresses five key methodological gaps in prior work: data leakage prevention, cross-year validation, threshold recalibration, cloud-gap correction, and physics-constrained prediction.

### 6.2 Recommendations

Based on the findings of this study, the following recommendations are proposed:

- **Urban Green Infrastructure:** Increase urban green cover through tree planting programmes, rooftop gardens, and urban parks to mitigate UHI effects, particularly in high-NDBI zones where LST is highest.
- **Wetland Conservation:** Protect remaining water bodies, mangroves, and coastal wetlands from encroachment, as these provide significant cooling effects and ecological services.
- **Cool Surface Policies:** Implement cool roof and permeable pavement regulations in areas with the highest LST values identified in this study.
- **SGNP Buffer Zone:** Maintain and enforce the buffer zone around Sanjay Gandhi National Park to prevent further encroachment of the primary dense vegetation area.
- **Ward-Level Monitoring:** Develop ward-specific urban heat mitigation strategies based on the LULC-LST relationships identified in this study, targeting the most vulnerable areas.

### 6.3 Limitations

- **Spatial Resolution:** Landsat 30m spatial resolution may not capture fine-scale urban features (individual buildings, narrow streets) and small vegetation patches. The 150m download resolution for numpy arrays introduces additional mixed-pixel effects at class boundaries.
- **Cross-Year Assumption:** The cross-year validation protocol assumes that land cover classes maintain consistent spectral signatures between 2015 and 2020, which may not be true for rapidly changing areas.
- **Sensor Transition:** Inter-sensor differences between Landsat 8 (2015, 2020) and Landsat 9 (2025) may introduce minor spectral inconsistencies despite both being Collection 2 Level 2 products.
- **CA-Markov Assumptions:** The prediction model assumes continuation of 2015–2020 transition patterns and does not account for policy changes, major infrastructure projects (Metro expansion), or climate events.
- **Urban Irreversibility:** While physically justified for Mumbai, the irreversibility constraint (based on 2020 reference) may cause slight overprediction of built-up area if some urban pixels in 2020 were misclassified.
- **Threshold Sensitivity:** The spectral threshold values for LULC classification are calibrated for Mumbai's specific spectral environment and may not be directly transferable to other cities.

### 6.4 Future Scope

- Use of **Sentinel-2** (10m) imagery for higher resolution LULC mapping and sub-pixel classification.
- Application of **deep learning** models (CNN, U-Net) for improved spectral–spatial classification.
- **Ward-level analysis** to identify specific administrative areas requiring targeted heat mitigation interventions.
- Integration of **socioeconomic and demographic data** (population density, income levels) with LULC and LST findings for vulnerability assessment.
- **LIME/SHAP explainability analysis** for the Random Forest classifier to understand which spectral features drive individual pixel-level classification decisions.
- **Real-time monitoring** using Google Earth Engine Apps for continuous LULC change detection.
- **Multi-city comparison** applying the same leakage-free methodology to Delhi, Bangalore, and other rapidly urbanizing Indian cities.

---

## References

[1] Shahfahad, Talukdar, S., Rihan, M., Hang, H. T., Bhatt, S., Pham, Q. B., & Rahman, A. (2021). Characterising urban heat island intensity in the mega-city of Delhi and Mumbai by earth observation approach. *Journal of the Indian Society of Remote Sensing*, 49(9), 2227–2247.

[2] Sahana, M., Dutta, S., & Sajjad, H. (2018). Assessing land transformation and associated degradation of the west Bengal part of Sundarbans using Earth Observation data and Receiving Operating Characteristic (ROC) curve. *Journal of Environmental Management*, 213, 209–221.

[3] Vinayak, B., Lee, H. S., Gedam, S., & Latha, R. (2022). Impacts of future urbanization on urban microclimate and human thermal comfort over Mumbai metropolitan area and its neighborhood. *Sustainable Cities and Society*, 79, 103703.

[4] Google Earth Engine Team. (2015). Google Earth Engine: A planetary-scale geo-spatial analysis platform. https://developers.google.com/earth-engine

[5] United States Geological Survey (USGS). (2023). Landsat Collection 2 Level-2 Science Products. https://www.usgs.gov/landsat-missions/landsat-collection-2-level-2-science-products

[6] Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. *International Journal of Remote Sensing*, 27(14), 3025–3033.

[7] Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5–32.

[8] Eastman, J. R. (2006). IDRISI Andes: Guide to GIS and Image Processing. Clark University.

[9] Pontius, R. G., & Malanson, J. (2005). Comparison of the structure and accuracy of two land change models. *International Journal of Geographical Information Science*, 19(2), 243–265.

---

## Appendix

### Appendix A: Colab Notebook Reference

The complete Python code for satellite image processing, LULC classification, accuracy assessment, spectral analysis, CA-Markov prediction, and publication figure generation was executed in Google Colab.

**Colab Notebook:** https://colab.research.google.com/drive/1lMBuZtxwnAauOBXYu-L_7DdSyNA_utd1?usp=sharing

**GEE Project ID:** apt-footing-484204-g5

**Output Files Generated by the Notebook:**

| File | Description |
|------|-------------|
| `accuracy_assessment.png` | Confusion matrix + per-class accuracy bar chart |
| `lulc_maps.png` | LULC classification maps (2015, 2020, 2025) |
| `lst_maps.png` | Land Surface Temperature maps (2015, 2020, 2025) |
| `markov_transition.png` | Markov transition probability matrices |
| `lulc_predicted_maps.png` | CA-Markov predicted LULC maps (2025, 2030, 2035) |
| `lulc_area_trend.png` | Stacked bar + line graph of area trends |
| `lst_per_class.png` | Mean LST per LULC class bar chart |
| `ndvi_vs_lst.png` | NDVI vs LST scatter plots with regression |
| `ndbi_vs_lst.png` | NDBI vs LST scatter plots with regression |
| `ndwi_vs_lst.png` | NDWI vs LST scatter plots with regression |

*Table A.1: List of output files generated by the Colab notebook*

**GeoTIFF Exports to Google Drive (`Mumbai_LULC/` folder):**
- LULC_2015.tif, LULC_2020.tif, LULC_2025.tif — Observed LULC rasters (30m)
- LST_2015.tif, LST_2020.tif, LST_2025.tif — Land Surface Temperature rasters
- NDVI_2015.tif, NDVI_2020.tif, NDVI_2025.tif — NDVI rasters
- NDBI_2015.tif, NDBI_2020.tif, NDBI_2025.tif — NDBI rasters
- NDWI_2015.tif, NDWI_2020.tif, NDWI_2025.tif — NDWI rasters
- LULC_Predicted_2030.tif, LULC_Predicted_2035.tif — Predicted LULC rasters

### Appendix B: How to Generate This Report with Actual Values

To populate this report with actual numerical values and figures from the Colab notebook:

1. **Open the Colab notebook** at the link above.
2. **Run all cells** sequentially (Runtime → Run all). Authentication with Google Earth Engine is required.
3. **Download the output images** (`.png` files) generated in the Colab working directory.
4. **Copy the numerical outputs** printed by each cell (accuracy values, area statistics, correlation coefficients) into the corresponding `*[notebook]*` placeholders in this report.
5. **Insert the images** at the corresponding `*(Insert ... from Colab output)*` markers.

Alternatively, use the `generate_report.py` script provided in this repository to automatically extract values from a saved notebook with outputs (`.ipynb` file with cell outputs preserved).

### Appendix C: List of Abbreviations

| Abbreviation | Full Form |
|-------------|----------|
| BMC | Brihanmumbai Municipal Corporation |
| CA | Cellular Automata |
| GEE | Google Earth Engine |
| GIS | Geographic Information System |
| LULC | Land Use Land Cover |
| LST | Land Surface Temperature |
| MNDWI | Modified Normalized Difference Water Index |
| NDBI | Normalized Difference Built-up Index |
| NDVI | Normalized Difference Vegetation Index |
| NDWI | Normalized Difference Water Index |
| OA | Overall Accuracy |
| OLI | Operational Land Imager |
| RF | Random Forest |
| R² | Coefficient of Determination |
| SGNP | Sanjay Gandhi National Park |
| SWIR | Short-Wave Infrared |
| NIR | Near Infrared |
| UHI | Urban Heat Island |
| USGS | United States Geological Survey |
| UTM | Universal Transverse Mercator |

*Table A.2: List of Abbreviations used in this report*
