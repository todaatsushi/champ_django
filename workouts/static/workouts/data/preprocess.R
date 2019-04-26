# setwd("~/Desktop/Personal Files/Education/Web Apps/champ/static")
library(tidyverse)

### GET DATA
# https://airtable.com/shrKZ9lPpw7EvjZ3X/tblvscpkbagqlWKkH & https://www.reddit.com/r/xxfitness/comments/8y0ljg/i_built_a_searchable_database_of_exercises/
data <- read.csv("exercises_raw.csv", stringsAsFactors = F) ; str(data)

# Change 1/0 into booleans
data[,12:19] <- lapply(data[,12:19], function(x){ifelse(x == 0, TRUE, FALSE)})

## Fix data
# Equipment
unique(data$Equipment)

# See unique values
sort(unique(rapply(strsplit(data$Equipment, ","), unique)))

# Equipment fix
fixes <- c(
        "Cabless" = "Cable",
        "Cables" = "Cable",
        "Cable" = "Cables",
        "Barbell & Rack" = "Barbell,Rack",
        "Body Weight" = "Bodyweight",
        "Dumbells. Band" = "Dumbbells,Band",
        "Kettlebells" = "Kettlebell",
        "Kettlebell" = "Kettlebells",
        "Plates" = "Plate",
        "Plate" = "Plates",
        "TRX/Rings" = "Rings/TRX"
)

# Replace fixed values
data$Equipment <-(data$Equipment %>% 
                          str_c(collapse = "__") %>%
                          str_replace_all(fixes) %>%
                          str_split("__"))[[1]]

# Finalised values
sort(unique(rapply(strsplit(data$Equipment, ","), unique)))

# Check Exercise.Type
sort(unique(rapply(strsplit(data$Exercise.Type, ","), unique)))

# Movement Type
sort(unique(rapply(strsplit(data$Movement.Type, ","), unique)))

# Compound/isolation
sort(unique(rapply(strsplit(data$Compound.Isolation, ","), unique)))

# Muscle Group
sort(unique(rapply(strsplit(data$Muscle.Group, ","), unique)))

# Major muscles
sort(unique(rapply(strsplit(data$Major.Muscle, ","), unique)))

fixes <- c(
        "Biceps" = "Bicep",
        "Bicep" = "Biceps"
)

data$Major.Muscle <-(data$Major.Muscle %>% 
                             str_c(collapse = "__") %>%
                             str_replace_all(fixes) %>%
                             str_split("__"))[[1]]

sort(unique(rapply(strsplit(data$Major.Muscle, ","), unique)))

# Minor muscles
sort(unique(rapply(strsplit(data$Minor.Muscle, ","), unique)))

# Fix "Legs" to leg muscles
data[grep("Legs", data$Minor.Muscle, fixed = TRUE),"Minor.Muscle"] <- "Quads,Glutes,Calves"

sort(unique(rapply(strsplit(data$Minor.Muscle, ","), unique)))

# Split multiple answer columns into lists
# data[,2:8] <- lapply(data[,2:8], function(x){ strsplit(x, ",", fixed = TRUE)})

# Drop notes/mods cols
data <- data[,-c(10:11)]

# Clean links
data$Example <- sub(".*\\(","" , data$Example) ; data$Example <- sub("\\)","" , data$Example)

# Export data
write.csv(data, file = "exercises_fin.csv")
