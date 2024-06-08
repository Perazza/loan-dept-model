{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c187051",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:04.729546Z",
     "iopub.status.busy": "2024-06-08T18:24:04.729019Z",
     "iopub.status.idle": "2024-06-08T18:24:05.795692Z",
     "shell.execute_reply": "2024-06-08T18:24:05.794369Z"
    },
    "papermill": {
     "duration": 1.081947,
     "end_time": "2024-06-08T18:24:05.798501",
     "exception": false,
     "start_time": "2024-06-08T18:24:04.716554",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/kaggle/input/loan-dataset/LoanDataset - LoansDatasest.csv\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e76bc4d8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:05.821769Z",
     "iopub.status.busy": "2024-06-08T18:24:05.821223Z",
     "iopub.status.idle": "2024-06-08T18:24:07.799967Z",
     "shell.execute_reply": "2024-06-08T18:24:07.798637Z"
    },
    "papermill": {
     "duration": 1.993313,
     "end_time": "2024-06-08T18:24:07.802951",
     "exception": false,
     "start_time": "2024-06-08T18:24:05.809638",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.preprocessing import LabelEncoder"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3597b465",
   "metadata": {
    "papermill": {
     "duration": 0.010022,
     "end_time": "2024-06-08T18:24:07.823803",
     "exception": false,
     "start_time": "2024-06-08T18:24:07.813781",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Import data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ef8cdeff",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:07.846917Z",
     "iopub.status.busy": "2024-06-08T18:24:07.846504Z",
     "iopub.status.idle": "2024-06-08T18:24:07.984583Z",
     "shell.execute_reply": "2024-06-08T18:24:07.983255Z"
    },
    "papermill": {
     "duration": 0.153364,
     "end_time": "2024-06-08T18:24:07.987904",
     "exception": false,
     "start_time": "2024-06-08T18:24:07.834540",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = pd.read_csv(r\"/kaggle/input/loan-dataset/LoanDataset - LoansDatasest.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "af0d4c48",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:08.012416Z",
     "iopub.status.busy": "2024-06-08T18:24:08.011935Z",
     "iopub.status.idle": "2024-06-08T18:24:08.100365Z",
     "shell.execute_reply": "2024-06-08T18:24:08.098731Z"
    },
    "papermill": {
     "duration": 0.10406,
     "end_time": "2024-06-08T18:24:08.103005",
     "exception": false,
     "start_time": "2024-06-08T18:24:07.998945",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 32586 entries, 0 to 32585\n",
      "Data columns (total 13 columns):\n",
      " #   Column               Non-Null Count  Dtype  \n",
      "---  ------               --------------  -----  \n",
      " 0   customer_id          32583 non-null  float64\n",
      " 1   customer_age         32586 non-null  int64  \n",
      " 2   customer_income      32586 non-null  object \n",
      " 3   home_ownership       32586 non-null  object \n",
      " 4   employment_duration  31691 non-null  float64\n",
      " 5   loan_intent          32586 non-null  object \n",
      " 6   loan_grade           32586 non-null  object \n",
      " 7   loan_amnt            32585 non-null  object \n",
      " 8   loan_int_rate        29470 non-null  float64\n",
      " 9   term_years           32586 non-null  int64  \n",
      " 10  historical_default   11849 non-null  object \n",
      " 11  cred_hist_length     32586 non-null  int64  \n",
      " 12  Current_loan_status  32582 non-null  object \n",
      "dtypes: float64(3), int64(3), object(7)\n",
      "memory usage: 3.2+ MB\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customer_id</th>\n",
       "      <th>customer_age</th>\n",
       "      <th>customer_income</th>\n",
       "      <th>home_ownership</th>\n",
       "      <th>employment_duration</th>\n",
       "      <th>loan_intent</th>\n",
       "      <th>loan_grade</th>\n",
       "      <th>loan_amnt</th>\n",
       "      <th>loan_int_rate</th>\n",
       "      <th>term_years</th>\n",
       "      <th>historical_default</th>\n",
       "      <th>cred_hist_length</th>\n",
       "      <th>Current_loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>22</td>\n",
       "      <td>59000</td>\n",
       "      <td>RENT</td>\n",
       "      <td>123.0</td>\n",
       "      <td>PERSONAL</td>\n",
       "      <td>C</td>\n",
       "      <td>£35,000.00</td>\n",
       "      <td>16.02</td>\n",
       "      <td>10</td>\n",
       "      <td>Y</td>\n",
       "      <td>3</td>\n",
       "      <td>DEFAULT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>21</td>\n",
       "      <td>9600</td>\n",
       "      <td>OWN</td>\n",
       "      <td>5.0</td>\n",
       "      <td>EDUCATION</td>\n",
       "      <td>A</td>\n",
       "      <td>£1,000.00</td>\n",
       "      <td>11.14</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NO DEFAULT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>25</td>\n",
       "      <td>9600</td>\n",
       "      <td>MORTGAGE</td>\n",
       "      <td>1.0</td>\n",
       "      <td>MEDICAL</td>\n",
       "      <td>B</td>\n",
       "      <td>£5,500.00</td>\n",
       "      <td>12.87</td>\n",
       "      <td>5</td>\n",
       "      <td>N</td>\n",
       "      <td>3</td>\n",
       "      <td>DEFAULT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>23</td>\n",
       "      <td>65500</td>\n",
       "      <td>RENT</td>\n",
       "      <td>4.0</td>\n",
       "      <td>MEDICAL</td>\n",
       "      <td>B</td>\n",
       "      <td>£35,000.00</td>\n",
       "      <td>15.23</td>\n",
       "      <td>10</td>\n",
       "      <td>N</td>\n",
       "      <td>2</td>\n",
       "      <td>DEFAULT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>24</td>\n",
       "      <td>54400</td>\n",
       "      <td>RENT</td>\n",
       "      <td>8.0</td>\n",
       "      <td>MEDICAL</td>\n",
       "      <td>B</td>\n",
       "      <td>£35,000.00</td>\n",
       "      <td>14.27</td>\n",
       "      <td>10</td>\n",
       "      <td>Y</td>\n",
       "      <td>4</td>\n",
       "      <td>DEFAULT</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   customer_id  customer_age customer_income home_ownership  \\\n",
       "0          1.0            22           59000           RENT   \n",
       "1          2.0            21            9600            OWN   \n",
       "2          3.0            25            9600       MORTGAGE   \n",
       "3          4.0            23           65500           RENT   \n",
       "4          5.0            24           54400           RENT   \n",
       "\n",
       "   employment_duration loan_intent loan_grade   loan_amnt  loan_int_rate  \\\n",
       "0                123.0    PERSONAL          C  £35,000.00          16.02   \n",
       "1                  5.0   EDUCATION          A   £1,000.00          11.14   \n",
       "2                  1.0     MEDICAL          B   £5,500.00          12.87   \n",
       "3                  4.0     MEDICAL          B  £35,000.00          15.23   \n",
       "4                  8.0     MEDICAL          B  £35,000.00          14.27   \n",
       "\n",
       "   term_years historical_default  cred_hist_length Current_loan_status  \n",
       "0          10                  Y                 3             DEFAULT  \n",
       "1           1                NaN                 2          NO DEFAULT  \n",
       "2           5                  N                 3             DEFAULT  \n",
       "3          10                  N                 2             DEFAULT  \n",
       "4          10                  Y                 4             DEFAULT  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.info()\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dbc7af39",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:08.127833Z",
     "iopub.status.busy": "2024-06-08T18:24:08.127401Z",
     "iopub.status.idle": "2024-06-08T18:24:08.244704Z",
     "shell.execute_reply": "2024-06-08T18:24:08.243364Z"
    },
    "papermill": {
     "duration": 0.13303,
     "end_time": "2024-06-08T18:24:08.247649",
     "exception": false,
     "start_time": "2024-06-08T18:24:08.114619",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customer_id</th>\n",
       "      <th>customer_age</th>\n",
       "      <th>customer_income</th>\n",
       "      <th>home_ownership</th>\n",
       "      <th>employment_duration</th>\n",
       "      <th>loan_intent</th>\n",
       "      <th>loan_grade</th>\n",
       "      <th>loan_amnt</th>\n",
       "      <th>loan_int_rate</th>\n",
       "      <th>term_years</th>\n",
       "      <th>historical_default</th>\n",
       "      <th>cred_hist_length</th>\n",
       "      <th>Current_loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>32583.000000</td>\n",
       "      <td>32586.000000</td>\n",
       "      <td>32586</td>\n",
       "      <td>32586</td>\n",
       "      <td>31691.000000</td>\n",
       "      <td>32586</td>\n",
       "      <td>32586</td>\n",
       "      <td>32585</td>\n",
       "      <td>29470.000000</td>\n",
       "      <td>32586.000000</td>\n",
       "      <td>11849</td>\n",
       "      <td>32586.000000</td>\n",
       "      <td>32582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4299</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>755</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>60000</td>\n",
       "      <td>RENT</td>\n",
       "      <td>NaN</td>\n",
       "      <td>EDUCATION</td>\n",
       "      <td>A</td>\n",
       "      <td>£10,000.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Y</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NO DEFAULT</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1046</td>\n",
       "      <td>16451</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6454</td>\n",
       "      <td>15661</td>\n",
       "      <td>2664</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6128</td>\n",
       "      <td>NaN</td>\n",
       "      <td>25742</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>16289.497806</td>\n",
       "      <td>27.732769</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.790161</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11.011553</td>\n",
       "      <td>4.761738</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.804026</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>9405.919628</td>\n",
       "      <td>6.360528</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.142746</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.240440</td>\n",
       "      <td>2.471107</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.055078</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.420000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>8144.500000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.900000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>16288.000000</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.990000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>24433.500000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>13.470000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>32581.000000</td>\n",
       "      <td>144.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>123.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>23.220000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         customer_id  customer_age customer_income home_ownership  \\\n",
       "count   32583.000000  32586.000000           32586          32586   \n",
       "unique           NaN           NaN            4299              4   \n",
       "top              NaN           NaN           60000           RENT   \n",
       "freq             NaN           NaN            1046          16451   \n",
       "mean    16289.497806     27.732769             NaN            NaN   \n",
       "std      9405.919628      6.360528             NaN            NaN   \n",
       "min         1.000000      3.000000             NaN            NaN   \n",
       "25%      8144.500000     23.000000             NaN            NaN   \n",
       "50%     16288.000000     26.000000             NaN            NaN   \n",
       "75%     24433.500000     30.000000             NaN            NaN   \n",
       "max     32581.000000    144.000000             NaN            NaN   \n",
       "\n",
       "        employment_duration loan_intent loan_grade   loan_amnt  loan_int_rate  \\\n",
       "count          31691.000000       32586      32586       32585   29470.000000   \n",
       "unique                  NaN           6          5         755            NaN   \n",
       "top                     NaN   EDUCATION          A  £10,000.00            NaN   \n",
       "freq                    NaN        6454      15661        2664            NaN   \n",
       "mean               4.790161         NaN        NaN         NaN      11.011553   \n",
       "std                4.142746         NaN        NaN         NaN       3.240440   \n",
       "min                0.000000         NaN        NaN         NaN       5.420000   \n",
       "25%                2.000000         NaN        NaN         NaN       7.900000   \n",
       "50%                4.000000         NaN        NaN         NaN      10.990000   \n",
       "75%                7.000000         NaN        NaN         NaN      13.470000   \n",
       "max              123.000000         NaN        NaN         NaN      23.220000   \n",
       "\n",
       "          term_years historical_default  cred_hist_length Current_loan_status  \n",
       "count   32586.000000              11849      32586.000000               32582  \n",
       "unique           NaN                  2               NaN                   2  \n",
       "top              NaN                  Y               NaN          NO DEFAULT  \n",
       "freq             NaN               6128               NaN               25742  \n",
       "mean        4.761738                NaN          5.804026                 NaN  \n",
       "std         2.471107                NaN          4.055078                 NaN  \n",
       "min         1.000000                NaN          2.000000                 NaN  \n",
       "25%         3.000000                NaN          3.000000                 NaN  \n",
       "50%         4.000000                NaN          4.000000                 NaN  \n",
       "75%         7.000000                NaN          8.000000                 NaN  \n",
       "max        10.000000                NaN         30.000000                 NaN  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe(include=\"all\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2538b643",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:08.272576Z",
     "iopub.status.busy": "2024-06-08T18:24:08.272128Z",
     "iopub.status.idle": "2024-06-08T18:24:09.496802Z",
     "shell.execute_reply": "2024-06-08T18:24:09.495552Z"
    },
    "papermill": {
     "duration": 1.240415,
     "end_time": "2024-06-08T18:24:09.499482",
     "exception": false,
     "start_time": "2024-06-08T18:24:08.259067",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "****************data****************\n",
      "customer_id                3\n",
      "customer_age               0\n",
      "customer_income            0\n",
      "home_ownership             0\n",
      "employment_duration      895\n",
      "loan_intent                0\n",
      "loan_grade                 0\n",
      "loan_amnt                  1\n",
      "loan_int_rate           3116\n",
      "term_years                 0\n",
      "historical_default     20737\n",
      "cred_hist_length           0\n",
      "Current_loan_status        4\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(data.isnull(), cbar=False)\n",
    "\n",
    "print('****************data****************')\n",
    "print(pd.isnull(data).sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3dcac290",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.526733Z",
     "iopub.status.busy": "2024-06-08T18:24:09.526256Z",
     "iopub.status.idle": "2024-06-08T18:24:09.538581Z",
     "shell.execute_reply": "2024-06-08T18:24:09.537174Z"
    },
    "papermill": {
     "duration": 0.029167,
     "end_time": "2024-06-08T18:24:09.541455",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.512288",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = data.drop('historical_default', axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e6bb7864",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.569225Z",
     "iopub.status.busy": "2024-06-08T18:24:09.568815Z",
     "iopub.status.idle": "2024-06-08T18:24:09.616801Z",
     "shell.execute_reply": "2024-06-08T18:24:09.615534Z"
    },
    "papermill": {
     "duration": 0.064972,
     "end_time": "2024-06-08T18:24:09.619627",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.554655",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "label_encoder = LabelEncoder()\n",
    "\n",
    "label_cols = (\n",
    "    'home_ownership', \n",
    "    'loan_intent', \n",
    "    'loan_grade'\n",
    ")\n",
    "\n",
    "# labeling columns and check if any of them have null values \n",
    "for label in label_cols:\n",
    "    if data[label].isnull().any():\n",
    "        print(f'there is null values in the column {label}')\n",
    "    else:\n",
    "        data[label] = label_encoder.fit_transform(data[label])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ef6d78fa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.647133Z",
     "iopub.status.busy": "2024-06-08T18:24:09.646732Z",
     "iopub.status.idle": "2024-06-08T18:24:09.658615Z",
     "shell.execute_reply": "2024-06-08T18:24:09.657431Z"
    },
    "papermill": {
     "duration": 0.028818,
     "end_time": "2024-06-08T18:24:09.661317",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.632499",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Apply the mapper dictionary to the column\n",
    "data['Current_loan_status'] = data['Current_loan_status'].map({'NO DEFAULT': 0, 'DEFAULT': 1})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "57a23f02",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.689332Z",
     "iopub.status.busy": "2024-06-08T18:24:09.688900Z",
     "iopub.status.idle": "2024-06-08T18:24:09.762303Z",
     "shell.execute_reply": "2024-06-08T18:24:09.761093Z"
    },
    "papermill": {
     "duration": 0.090464,
     "end_time": "2024-06-08T18:24:09.765198",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.674734",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data['loan_amnt'] = data['loan_amnt'].str.replace('£', '').str.replace(',', '').astype(float)\n",
    "data['customer_income'] = data['customer_income'].str.replace(',', '').astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fa461389",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.792481Z",
     "iopub.status.busy": "2024-06-08T18:24:09.792051Z",
     "iopub.status.idle": "2024-06-08T18:24:09.818412Z",
     "shell.execute_reply": "2024-06-08T18:24:09.817334Z"
    },
    "papermill": {
     "duration": 0.043097,
     "end_time": "2024-06-08T18:24:09.821123",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.778026",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customer_id</th>\n",
       "      <th>customer_age</th>\n",
       "      <th>customer_income</th>\n",
       "      <th>home_ownership</th>\n",
       "      <th>employment_duration</th>\n",
       "      <th>loan_intent</th>\n",
       "      <th>loan_grade</th>\n",
       "      <th>loan_amnt</th>\n",
       "      <th>loan_int_rate</th>\n",
       "      <th>term_years</th>\n",
       "      <th>cred_hist_length</th>\n",
       "      <th>Current_loan_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>22</td>\n",
       "      <td>59000</td>\n",
       "      <td>3</td>\n",
       "      <td>123.0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>35000.0</td>\n",
       "      <td>16.02</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>21</td>\n",
       "      <td>9600</td>\n",
       "      <td>2</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1000.0</td>\n",
       "      <td>11.14</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>25</td>\n",
       "      <td>9600</td>\n",
       "      <td>0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>5500.0</td>\n",
       "      <td>12.87</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>23</td>\n",
       "      <td>65500</td>\n",
       "      <td>3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35000.0</td>\n",
       "      <td>15.23</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>24</td>\n",
       "      <td>54400</td>\n",
       "      <td>3</td>\n",
       "      <td>8.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35000.0</td>\n",
       "      <td>14.27</td>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32581</th>\n",
       "      <td>32577.0</td>\n",
       "      <td>57</td>\n",
       "      <td>53000</td>\n",
       "      <td>0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>5800.0</td>\n",
       "      <td>13.16</td>\n",
       "      <td>7</td>\n",
       "      <td>30</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32582</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>54</td>\n",
       "      <td>120000</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>17625.0</td>\n",
       "      <td>7.49</td>\n",
       "      <td>4</td>\n",
       "      <td>19</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32583</th>\n",
       "      <td>32579.0</td>\n",
       "      <td>65</td>\n",
       "      <td>76000</td>\n",
       "      <td>3</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>35000.0</td>\n",
       "      <td>10.99</td>\n",
       "      <td>5</td>\n",
       "      <td>28</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32584</th>\n",
       "      <td>32580.0</td>\n",
       "      <td>56</td>\n",
       "      <td>150000</td>\n",
       "      <td>0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>15000.0</td>\n",
       "      <td>11.48</td>\n",
       "      <td>6</td>\n",
       "      <td>26</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32585</th>\n",
       "      <td>32581.0</td>\n",
       "      <td>99</td>\n",
       "      <td>42000</td>\n",
       "      <td>3</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>6475.0</td>\n",
       "      <td>9.99</td>\n",
       "      <td>6</td>\n",
       "      <td>30</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>32586 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       customer_id  customer_age  customer_income  home_ownership  \\\n",
       "0              1.0            22            59000               3   \n",
       "1              2.0            21             9600               2   \n",
       "2              3.0            25             9600               0   \n",
       "3              4.0            23            65500               3   \n",
       "4              5.0            24            54400               3   \n",
       "...            ...           ...              ...             ...   \n",
       "32581      32577.0            57            53000               0   \n",
       "32582      32578.0            54           120000               0   \n",
       "32583      32579.0            65            76000               3   \n",
       "32584      32580.0            56           150000               0   \n",
       "32585      32581.0            99            42000               3   \n",
       "\n",
       "       employment_duration  loan_intent  loan_grade  loan_amnt  loan_int_rate  \\\n",
       "0                    123.0            4           2    35000.0          16.02   \n",
       "1                      5.0            1           0     1000.0          11.14   \n",
       "2                      1.0            3           1     5500.0          12.87   \n",
       "3                      4.0            3           1    35000.0          15.23   \n",
       "4                      8.0            3           1    35000.0          14.27   \n",
       "...                    ...          ...         ...        ...            ...   \n",
       "32581                  1.0            4           2     5800.0          13.16   \n",
       "32582                  4.0            4           0    17625.0           7.49   \n",
       "32583                  3.0            2           1    35000.0          10.99   \n",
       "32584                  5.0            4           1    15000.0          11.48   \n",
       "32585                  2.0            3           1     6475.0           9.99   \n",
       "\n",
       "       term_years  cred_hist_length  Current_loan_status  \n",
       "0              10                 3                  1.0  \n",
       "1               1                 2                  0.0  \n",
       "2               5                 3                  1.0  \n",
       "3              10                 2                  1.0  \n",
       "4              10                 4                  1.0  \n",
       "...           ...               ...                  ...  \n",
       "32581           7                30                  0.0  \n",
       "32582           4                19                  0.0  \n",
       "32583           5                28                  1.0  \n",
       "32584           6                26                  0.0  \n",
       "32585           6                30                  0.0  \n",
       "\n",
       "[32586 rows x 12 columns]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37bd6bff",
   "metadata": {
    "papermill": {
     "duration": 0.012556,
     "end_time": "2024-06-08T18:24:09.846598",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.834042",
     "status": "completed"
    },
    "tags": []
   },
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "462f5b98",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.874471Z",
     "iopub.status.busy": "2024-06-08T18:24:09.873978Z",
     "iopub.status.idle": "2024-06-08T18:24:09.884072Z",
     "shell.execute_reply": "2024-06-08T18:24:09.882732Z"
    },
    "papermill": {
     "duration": 0.027348,
     "end_time": "2024-06-08T18:24:09.887017",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.859669",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data['employment_duration'] = data['employment_duration'].fillna(data['employment_duration'].mean())\n",
    "data['loan_int_rate'] = data['loan_int_rate'].fillna(data['loan_int_rate'].median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2cd9aff8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.914794Z",
     "iopub.status.busy": "2024-06-08T18:24:09.914384Z",
     "iopub.status.idle": "2024-06-08T18:24:09.924040Z",
     "shell.execute_reply": "2024-06-08T18:24:09.922721Z"
    },
    "papermill": {
     "duration": 0.026984,
     "end_time": "2024-06-08T18:24:09.926971",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.899987",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = data.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "12b73882",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.956412Z",
     "iopub.status.busy": "2024-06-08T18:24:09.955938Z",
     "iopub.status.idle": "2024-06-08T18:24:09.965437Z",
     "shell.execute_reply": "2024-06-08T18:24:09.963812Z"
    },
    "papermill": {
     "duration": 0.026619,
     "end_time": "2024-06-08T18:24:09.968044",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.941425",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "****************data****************\n",
      "customer_id            0\n",
      "customer_age           0\n",
      "customer_income        0\n",
      "home_ownership         0\n",
      "employment_duration    0\n",
      "loan_intent            0\n",
      "loan_grade             0\n",
      "loan_amnt              0\n",
      "loan_int_rate          0\n",
      "term_years             0\n",
      "cred_hist_length       0\n",
      "Current_loan_status    0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print('****************data****************')\n",
    "print(pd.isnull(data).sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d421073a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:09.995862Z",
     "iopub.status.busy": "2024-06-08T18:24:09.995453Z",
     "iopub.status.idle": "2024-06-08T18:24:10.062963Z",
     "shell.execute_reply": "2024-06-08T18:24:10.061711Z"
    },
    "papermill": {
     "duration": 0.084643,
     "end_time": "2024-06-08T18:24:10.065656",
     "exception": false,
     "start_time": "2024-06-08T18:24:09.981013",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>customer_id</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>16289.238811</td>\n",
       "      <td>9405.973303</td>\n",
       "      <td>1.00</td>\n",
       "      <td>8144.25</td>\n",
       "      <td>16286.50</td>\n",
       "      <td>24434.75</td>\n",
       "      <td>32581.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>customer_age</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>27.732703</td>\n",
       "      <td>6.361206</td>\n",
       "      <td>3.00</td>\n",
       "      <td>23.00</td>\n",
       "      <td>26.00</td>\n",
       "      <td>30.00</td>\n",
       "      <td>144.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>customer_income</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>66075.162318</td>\n",
       "      <td>61987.592558</td>\n",
       "      <td>4000.00</td>\n",
       "      <td>38500.00</td>\n",
       "      <td>55000.00</td>\n",
       "      <td>79200.00</td>\n",
       "      <td>6000000.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>home_ownership</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>1.676407</td>\n",
       "      <td>1.433109</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>3.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>employment_duration</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>4.790018</td>\n",
       "      <td>4.085790</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>7.00</td>\n",
       "      <td>123.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>loan_intent</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>2.533673</td>\n",
       "      <td>1.731063</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>5.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>loan_grade</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>0.859905</td>\n",
       "      <td>1.009556</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.00</td>\n",
       "      <td>1.00</td>\n",
       "      <td>4.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>loan_amnt</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>9755.841365</td>\n",
       "      <td>21774.005616</td>\n",
       "      <td>500.00</td>\n",
       "      <td>5000.00</td>\n",
       "      <td>8000.00</td>\n",
       "      <td>12200.00</td>\n",
       "      <td>3500000.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>loan_int_rate</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>11.009320</td>\n",
       "      <td>3.081849</td>\n",
       "      <td>5.42</td>\n",
       "      <td>8.49</td>\n",
       "      <td>10.99</td>\n",
       "      <td>13.11</td>\n",
       "      <td>23.22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>term_years</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>4.761465</td>\n",
       "      <td>2.470934</td>\n",
       "      <td>1.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>7.00</td>\n",
       "      <td>10.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cred_hist_length</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>5.803702</td>\n",
       "      <td>4.055323</td>\n",
       "      <td>2.00</td>\n",
       "      <td>3.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>8.00</td>\n",
       "      <td>30.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Current_loan_status</th>\n",
       "      <td>32578.0</td>\n",
       "      <td>0.209896</td>\n",
       "      <td>0.407241</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       count          mean           std      min       25%  \\\n",
       "customer_id          32578.0  16289.238811   9405.973303     1.00   8144.25   \n",
       "customer_age         32578.0     27.732703      6.361206     3.00     23.00   \n",
       "customer_income      32578.0  66075.162318  61987.592558  4000.00  38500.00   \n",
       "home_ownership       32578.0      1.676407      1.433109     0.00      0.00   \n",
       "employment_duration  32578.0      4.790018      4.085790     0.00      2.00   \n",
       "loan_intent          32578.0      2.533673      1.731063     0.00      1.00   \n",
       "loan_grade           32578.0      0.859905      1.009556     0.00      0.00   \n",
       "loan_amnt            32578.0   9755.841365  21774.005616   500.00   5000.00   \n",
       "loan_int_rate        32578.0     11.009320      3.081849     5.42      8.49   \n",
       "term_years           32578.0      4.761465      2.470934     1.00      3.00   \n",
       "cred_hist_length     32578.0      5.803702      4.055323     2.00      3.00   \n",
       "Current_loan_status  32578.0      0.209896      0.407241     0.00      0.00   \n",
       "\n",
       "                          50%       75%         max  \n",
       "customer_id          16286.50  24434.75    32581.00  \n",
       "customer_age            26.00     30.00      144.00  \n",
       "customer_income      55000.00  79200.00  6000000.00  \n",
       "home_ownership           3.00      3.00        3.00  \n",
       "employment_duration      4.00      7.00      123.00  \n",
       "loan_intent              3.00      4.00        5.00  \n",
       "loan_grade               1.00      1.00        4.00  \n",
       "loan_amnt             8000.00  12200.00  3500000.00  \n",
       "loan_int_rate           10.99     13.11       23.22  \n",
       "term_years               4.00      7.00       10.00  \n",
       "cred_hist_length         4.00      8.00       30.00  \n",
       "Current_loan_status      0.00      0.00        1.00  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4d4205b4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:10.095073Z",
     "iopub.status.busy": "2024-06-08T18:24:10.094638Z",
     "iopub.status.idle": "2024-06-08T18:24:10.986738Z",
     "shell.execute_reply": "2024-06-08T18:24:10.985453Z"
    },
    "papermill": {
     "duration": 0.912493,
     "end_time": "2024-06-08T18:24:10.991927",
     "exception": false,
     "start_time": "2024-06-08T18:24:10.079434",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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zZo18xgXoFGjRuj1enQV2ng1atSIjIwMAHbv3k1RURENGnge7KWlpRw7duy8+T148GClAES/fv147733AAgMDKRTp06sXr0ak8mEyWTigQce4KWXXqKoqIg1a9YwaJDn4ELt2rVDr3dfIISHh7N3717AGWBxOBy0bu15MVReXu5RBpPJ5LEug4ODmTRpEqNGjWLEiBEMHz6ciRMnEh4e7kpz9ro7s+7PpU+fPpX+njFjRrXpy8vLKS/3PHE57OXoDRffx29AN18euMXdHHr6x2kXvYyLsS++lKffTMLPR8/wvn48NSmUae8kU1BUt2em7m0M3DrM3dmyrm/ktx6ycSjRgb+PwrCuJu4dY+HducXYz3oKEt5Ax/3XefPr5vJ66bs4vH8DnnqguevvadMP13iZj9/XjOZRFh79x4EaL0vUzIhBoTw92V3PPfPq3hov86m/taJFEx8efrby09Dlq9PZujOXBsEmbhvfmP97NpaHntmJ1XZlPeUVtSPuh1fITo3nlie+uay/262NgVuGulvSfbywboOY2w7ZOJxox9+iY0g3E/de482MH0oq1ed/VsGNmnPv3xdQXlrI4Z3LWDznWW5/6qs6CTB0aaVnwiB3oPPzOrhJv1BHklQWbbRx00ATtw0DhwNWbLfRIkKPdrpK8/OGmweb2HbYzs6jdryMCqN6GLl7lJlPfqlZ3ru1NjBxiPu67pNf6j5YbzbCA9d5k56rsnSLO/KiKGDQK8xbU8bh060gvlhaxv/d50Orxvp6uX65FCt//oydG39l8ouzMJoqXzM77DbmvDcFTdO4+S8v1kMOxZ/VHz64cPbbCBRFuajBCKua/1zLLCoqIjw83GPMgjMCAwMv+HfPZfDgwaxevRqz2cygQYMIDg6mbdu2rFu3jjVr1jBlypTzlqFifvV6Pdu3b/cIQAD4+rqjlN7e3h5dHgBmzZrFY489xtKlS/n+++954YUXWLFiBb179z7v79aW6dOn88orngPMte35GLG9H7/oZW3dV0z8SfeI/obTgzYG+unJK3CfLAL89LXSfaHcqpGWZScty078yXL++0IUw3r7M39lXo2XfS57j9tJSCty/W3QO8vp5+PZEsHPopCcWfVJsrhUw6G6n2pUnKfgrNYXZVYos6pk5kFCailvPORHp2gD2w+7uwmEBet45EYLG/bZWLalfoaVX78t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CkpIcsXiAhERyZKfnx8+/PBDDB06VHQUIiKibjtx4gQCAwPRq1cvzJ07F4MGDQIA1NTUICMjA+3t7VCpVHB0dBSclOSGxQUiIpKlnTt3QqlUIjMzE+7u7qLjEBERdduRI0fwyiuv4LPPPsPV2zlJkjBu3DhkZGTA09NTcEKSIxYXiIhIlhobG/HMM8/gyy+/RJ8+ffSGY505c0ZQMiIiou755ZdfUFtbC41GAx8fH9jb24uORDLG4gIREclSWFgY6uvrERUVBUdHR72BjhEREYKSEREREfU8LC4QEZEs9enTByUlJQgICBAdhYiIiKjHU4gOQEREJIKvry+am5tFxyAiIiIyCSwuEBGRLK1atQoJCQn4/PPPcfr0aZw7d07nDxERERF1H7dFEBGRLCkU/19fv3begkajgSRJaG9vFxGLiIiIqEfqLToAERGRCEVFRaIjEBEREZkMbosgIiJZevTRR6FQKLBhwwYsWrQI3t7eePTRR1FfX49evXqJjkdERETUo7C4QEREsrR161aMGzcOVlZWKC8vx6+//goAOHv2LFJSUgSnIyIiIupZWFwgIiJZeuONN5CZmYkNGzbAzMxMuz5y5EioVCqByYiIiIh6HhYXiIhIlr7//nuMGjVKb93Ozg5NTU3GD0RERETUg7G4QEREstS/f3/U1tbqrX/11Vfw8vISkIiIiIio52JxgYiIZCk6Ohrz5s1DaWkpJEnCsWPH8MEHHyAxMRGvvPKK6HhEREREPQqPoiQiIllatGgROjo6MHr0aFy8eBGjRo2ChYUFEhMTERMTIzoeERERUY8iaTQajegQREREorS2tqK2thZqtRp+fn7o27ev6EhEREREPQ6LC0RERERERER0SzhzgYiIiIiIiIhuCYsLRERERERERHRLWFwgIiIiIiIiolvC4gIRERERERER3RIWF4iIiIiIiIjolrC4QERERERERES3hMUFIiIiIiIiIrolLC4QERERERER0S35P0pQotXjGtsKAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1200x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "numeric_cols = data.select_dtypes(include=np.number).columns\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm')\n",
    "plt.title('Correlation Matrix')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5dca3b4f",
   "metadata": {
    "papermill": {
     "duration": 0.015731,
     "end_time": "2024-06-08T18:24:11.023786",
     "exception": false,
     "start_time": "2024-06-08T18:24:11.008055",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Check balance to binary classification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3590424c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:11.057933Z",
     "iopub.status.busy": "2024-06-08T18:24:11.057503Z",
     "iopub.status.idle": "2024-06-08T18:24:11.068987Z",
     "shell.execute_reply": "2024-06-08T18:24:11.067637Z"
    },
    "papermill": {
     "duration": 0.032165,
     "end_time": "2024-06-08T18:24:11.072180",
     "exception": false,
     "start_time": "2024-06-08T18:24:11.040015",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current_loan_status\n",
      "0.0    0.790104\n",
      "1.0    0.209896\n",
      "Name: count, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "count = data['Current_loan_status'].count()\n",
    "classCount = data['Current_loan_status'].value_counts()\n",
    "\n",
    "balanced =  classCount / count\n",
    "\n",
    "print(balanced)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1d17a40c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:11.106311Z",
     "iopub.status.busy": "2024-06-08T18:24:11.105901Z",
     "iopub.status.idle": "2024-06-08T18:24:12.815325Z",
     "shell.execute_reply": "2024-06-08T18:24:12.813960Z"
    },
    "papermill": {
     "duration": 1.730257,
     "end_time": "2024-06-08T18:24:12.818401",
     "exception": false,
     "start_time": "2024-06-08T18:24:11.088144",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import lightgbm as lgb\n",
    "from lightgbm import LGBMClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.metrics import precision_score, recall_score, f1_score, classification_report, roc_curve, auc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7929db95",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:12.853781Z",
     "iopub.status.busy": "2024-06-08T18:24:12.853084Z",
     "iopub.status.idle": "2024-06-08T18:24:12.859863Z",
     "shell.execute_reply": "2024-06-08T18:24:12.858582Z"
    },
    "papermill": {
     "duration": 0.027154,
     "end_time": "2024-06-08T18:24:12.862564",
     "exception": false,
     "start_time": "2024-06-08T18:24:12.835410",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "features = [ \n",
    "     \"customer_age\"\n",
    "    ,\"customer_income\"\n",
    "    ,\"home_ownership\"\n",
    "    ,\"employment_duration\"\n",
    "    ,\"loan_intent\"\n",
    "    ,\"loan_grade\"\n",
    "    ,\"loan_amnt\"\n",
    "    ,\"loan_int_rate\"\n",
    "    ,\"term_years\"\n",
    "    ,\"cred_hist_length\"\n",
    "]\n",
    "\n",
    "label = \"Current_loan_status\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "101914e0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:12.897139Z",
     "iopub.status.busy": "2024-06-08T18:24:12.896712Z",
     "iopub.status.idle": "2024-06-08T18:24:12.904845Z",
     "shell.execute_reply": "2024-06-08T18:24:12.903569Z"
    },
    "papermill": {
     "duration": 0.029132,
     "end_time": "2024-06-08T18:24:12.907631",
     "exception": false,
     "start_time": "2024-06-08T18:24:12.878499",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "y = data[label]\n",
    "x = data[features]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "202bd403",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:12.941575Z",
     "iopub.status.busy": "2024-06-08T18:24:12.941133Z",
     "iopub.status.idle": "2024-06-08T18:24:12.956129Z",
     "shell.execute_reply": "2024-06-08T18:24:12.954986Z"
    },
    "papermill": {
     "duration": 0.035327,
     "end_time": "2024-06-08T18:24:12.958855",
     "exception": false,
     "start_time": "2024-06-08T18:24:12.923528",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8296ad6b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:12.992744Z",
     "iopub.status.busy": "2024-06-08T18:24:12.992296Z",
     "iopub.status.idle": "2024-06-08T18:24:13.902904Z",
     "shell.execute_reply": "2024-06-08T18:24:13.901594Z"
    },
    "papermill": {
     "duration": 0.931728,
     "end_time": "2024-06-08T18:24:13.906572",
     "exception": false,
     "start_time": "2024-06-08T18:24:12.974844",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[LightGBM] [Warning] bagging_freq is set=5, subsample_freq=0 will be ignored. Current value: bagging_freq=5\n",
      "[LightGBM] [Warning] feature_fraction is set=0.9, colsample_bytree=1.0 will be ignored. Current value: feature_fraction=0.9\n",
      "[LightGBM] [Warning] bagging_fraction is set=0.8, subsample=1.0 will be ignored. Current value: bagging_fraction=0.8\n",
      "[LightGBM] [Warning] bagging_freq is set=5, subsample_freq=0 will be ignored. Current value: bagging_freq=5\n",
      "[LightGBM] [Warning] feature_fraction is set=0.9, colsample_bytree=1.0 will be ignored. Current value: feature_fraction=0.9\n",
      "[LightGBM] [Warning] bagging_fraction is set=0.8, subsample=1.0 will be ignored. Current value: bagging_fraction=0.8\n"
     ]
    }
   ],
   "source": [
    "# Using random parameters, use optuna or hypertune\n",
    "\n",
    "params = {\n",
    "    'objective': 'binary',  # Binary classification objective\n",
    "    'metric': 'binary_error',  # Metric to evaluate the model\n",
    "    'num_leaves': 31,  # Maximum number of leaves in one tree\n",
    "    'learning_rate': 0.05,  # Learning rate of gradient boosting\n",
    "    'feature_fraction': 0.9,  # Percentage of features to consider in each iteration\n",
    "    'bagging_fraction': 0.8,  # Percentage of data to use in each iteration\n",
    "    'bagging_freq': 5,  # Frequency for bagging\n",
    "    'verbose': 0  # Verbosity\n",
    "}\n",
    "\n",
    "boolean_cols = list(X_train.select_dtypes(include='bool').columns)\n",
    "numeric_cols = list(X_train.select_dtypes(include='number').columns)\n",
    "categorical_cols = list(X_train.select_dtypes(exclude=['bool', 'number']).columns)\n",
    "\n",
    "# Pipeline para colunas booleanas\n",
    "bool_pipeline = Pipeline(steps=[\n",
    "    # Converter booleanos para tipo objeto para codificação one-hot\n",
    "    (\"cast_type\", FunctionTransformer(lambda df: df.astype(object))),\n",
    "    # Aplicar codificação one-hot\n",
    "    (\"onehot\", OneHotEncoder(handle_unknown=\"ignore\", drop=\"first\")),\n",
    "])\n",
    "\n",
    "# Pipeline para colunas numéricas\n",
    "numerical_pipeline = Pipeline(steps=[\n",
    "    # Converter para numérico, tratando erros\n",
    "    (\"converter\", FunctionTransformer(lambda df: df.apply(pd.to_numeric, errors='coerce'))),\n",
    "    # Imputação da média para valores ausentes\n",
    "    (\"impute_mean\", SimpleImputer(strategy=\"mean\")),\n",
    "    # Padronização das colunas numéricas\n",
    "    (\"standardizer\", StandardScaler()),\n",
    "])\n",
    "\n",
    "# Pipeline para colunas categóricas\n",
    "one_hot_pipeline = Pipeline(steps=[\n",
    "    # Imputação com valor constante \"0\" para valores ausentes\n",
    "    (\"impute_zero\", SimpleImputer(strategy=\"constant\", fill_value=\"0\")),\n",
    "    # Codificação one-hot\n",
    "    (\"one_hot_encoder\", OneHotEncoder(handle_unknown=\"ignore\")),\n",
    "])\n",
    "\n",
    "transformers = [\n",
    "    (\"boolean\", bool_pipeline, boolean_cols),\n",
    "    (\"numerical\", numerical_pipeline, numeric_cols),\n",
    "    (\"onehot\", one_hot_pipeline, categorical_cols),\n",
    "]\n",
    "\n",
    "# Preprocessador final\n",
    "preprocessor = ColumnTransformer(transformers, remainder=\"passthrough\")\n",
    "\n",
    "num_round = 100\n",
    "lgbmc_classifier = LGBMClassifier(**params, random_state = 42)\n",
    "\n",
    "\n",
    "model_pipe = Pipeline(steps=[\n",
    "                (\"preprocessor\", preprocessor),\n",
    "                ('model', lgbmc_classifier)\n",
    "])\n",
    "\n",
    "\n",
    "model = model_pipe.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5e891f74",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:13.955012Z",
     "iopub.status.busy": "2024-06-08T18:24:13.954586Z",
     "iopub.status.idle": "2024-06-08T18:24:14.036211Z",
     "shell.execute_reply": "2024-06-08T18:24:14.034692Z"
    },
    "papermill": {
     "duration": 0.109191,
     "end_time": "2024-06-08T18:24:14.039120",
     "exception": false,
     "start_time": "2024-06-08T18:24:13.929929",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[LightGBM] [Warning] bagging_freq is set=5, subsample_freq=0 will be ignored. Current value: bagging_freq=5\n",
      "[LightGBM] [Warning] feature_fraction is set=0.9, colsample_bytree=1.0 will be ignored. Current value: feature_fraction=0.9\n",
      "[LightGBM] [Warning] bagging_fraction is set=0.8, subsample=1.0 will be ignored. Current value: bagging_fraction=0.8\n"
     ]
    }
   ],
   "source": [
    "y_pred = model_pipe.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e354e501",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:14.074532Z",
     "iopub.status.busy": "2024-06-08T18:24:14.073267Z",
     "iopub.status.idle": "2024-06-08T18:24:14.099637Z",
     "shell.execute_reply": "2024-06-08T18:24:14.098371Z"
    },
    "papermill": {
     "duration": 0.047315,
     "end_time": "2024-06-08T18:24:14.102600",
     "exception": false,
     "start_time": "2024-06-08T18:24:14.055285",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "precision = precision_score(y_test, y_pred, average='weighted')\n",
    "recall = recall_score(y_test, y_pred, average='weighted')\n",
    "f1 = f1_score(y_test, y_pred, average='weighted')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3afb9ab8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:14.141312Z",
     "iopub.status.busy": "2024-06-08T18:24:14.140847Z",
     "iopub.status.idle": "2024-06-08T18:24:14.147420Z",
     "shell.execute_reply": "2024-06-08T18:24:14.146195Z"
    },
    "papermill": {
     "duration": 0.031599,
     "end_time": "2024-06-08T18:24:14.150918",
     "exception": false,
     "start_time": "2024-06-08T18:24:14.119319",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9282319200380474 0.9280540208717004 0.9241812522159513\n"
     ]
    }
   ],
   "source": [
    "print(precision, recall, f1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "4c8a00fa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:14.195276Z",
     "iopub.status.busy": "2024-06-08T18:24:14.194431Z",
     "iopub.status.idle": "2024-06-08T18:24:14.228225Z",
     "shell.execute_reply": "2024-06-08T18:24:14.226538Z"
    },
    "papermill": {
     "duration": 0.055061,
     "end_time": "2024-06-08T18:24:14.231136",
     "exception": false,
     "start_time": "2024-06-08T18:24:14.176075",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "         0.0       0.93      0.99      0.96      6459\n",
      "         1.0       0.93      0.70      0.80      1686\n",
      "\n",
      "    accuracy                           0.93      8145\n",
      "   macro avg       0.93      0.85      0.88      8145\n",
      "weighted avg       0.93      0.93      0.92      8145\n",
      "\n"
     ]
    }
   ],
   "source": [
    "report = classification_report(y_test, y_pred)\n",
    "print(report)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0993294c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:14.267919Z",
     "iopub.status.busy": "2024-06-08T18:24:14.267483Z",
     "iopub.status.idle": "2024-06-08T18:24:14.276694Z",
     "shell.execute_reply": "2024-06-08T18:24:14.275464Z"
    },
    "papermill": {
     "duration": 0.031058,
     "end_time": "2024-06-08T18:24:14.279723",
     "exception": false,
     "start_time": "2024-06-08T18:24:14.248665",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "fpr, tpr, thresholds = roc_curve(y_test, y_pred)\n",
    "roc_auc = auc(fpr, tpr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c8a5849a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T18:24:14.316100Z",
     "iopub.status.busy": "2024-06-08T18:24:14.315675Z",
     "iopub.status.idle": "2024-06-08T18:24:14.653442Z",
     "shell.execute_reply": "2024-06-08T18:24:14.651985Z"
    },
    "papermill": {
     "duration": 0.359599,
     "end_time": "2024-06-08T18:24:14.656768",
     "exception": false,
     "start_time": "2024-06-08T18:24:14.297169",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(fpr, tpr, color='blue', label='ROC Curve')\n",
    "plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='Random Guessing')\n",
    "plt.xlabel('False Positive Rate (FPR)')\n",
    "plt.ylabel('True Positive Rate (TPR)')\n",
    "plt.title('Receiver Operating Characteristic (ROC) Curve')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 5170437,
     "sourceId": 8634488,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30732,
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 14.676223,
   "end_time": "2024-06-08T18:24:15.506490",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-06-08T18:24:00.830267",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
