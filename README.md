# data-visualization


Visualizing my measured values through time

myvars <- c("Date", "Site", "TP", "Zone")
TP_Data <- data[myvars]

TP_Graph <- ggline(TP_Data, x = "Date", y = "TP", color = "Zone",   
       add = c("mean_se")) +
  geom_jitter(aes(colour=Zone), width = .25)+
  theme_gray() +
  scale_x_discrete(labels = c("July-17", "July-25", "Aug-1", "Aug-8", "Aug-18", "Aug-23", "Oct-18"))  
  #ggtitle("Field Measured Total Phosphorus (mg/L)") 


TP_Graph.labs <- TP_Graph + labs(title = "Field Measured Total Phosphorus Concentration (mg/L)",
                           x = "Date Measured", y = "TP Concentration")

axis.format <- element_text(size = 15)

TP_Graph.final <- TP_Graph.labs + theme(title = axis.format, axis.title = axis.format)

TP_Graph.final

ggsave("TotalPGraph.png", TP_Graph.final, width = 10, height = 7)

getwd()
