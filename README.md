# data-visualization


Visualizing my measured values through time



```{r}
library(datasets)
library(ggplot2)
library(dplyr)
library(ggpubr)


setwd("E:/Thesis/Pandas_csv")
data <- read.csv('All_data.csv', header = TRUE, sep = ',')

myvars <- c("Date", "Site", "TP", "Zone")
TP_Data <- data[myvars]

TSS_Graph <- ggline(TSS_Data, x = "Date", y = "TSS", linetype = "Zone",   
       add = c("mean_se")) +
  geom_jitter(aes(shape=Zone), size = 2, width = .20)+
  theme_classic() +
  scale_x_discrete(labels = c("July-17", "July-25", "Aug-1", "Aug-8", "Aug-18", "Aug-23", "Oct-18"))
  #ggtitle("Means of Total Suspended Solids Values") 

TSS_Graph.labs <- TSS_Graph + labs(title = "Field Measured Total Suspended Solid Concentration (mg/L)",
                           x = "Date Measured", y = "TP Concentration")

axis.format <- element_text(size = 15)

TSS_Graph.final <- TSS_Graph.labs + theme(title = axis.format, axis.title = axis.format)

TSS_Graph.final

```
