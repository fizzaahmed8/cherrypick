restaurant = read.csv("yelp_academic_dataset_business_train.csv")
restaurant_AZ = restaurant[restaurant$state == "AZ",]
restaurant_WI = restaurant[restaurant$state == "WI",]
restaurant_NC = restaurant[restaurant$state == "NC",]
restaurant_NV = restaurant[restaurant$state == "NV",]
restaurant_PA = restaurant[restaurant$state == "PA",]
restaurant_OH = restaurant[restaurant$state == "OH",]

km_AZ <- kmeans(cbind(restaurant_AZ$latitude, restaurant_AZ$longitude), 
             centers = 21)
plot(restaurant_AZ$longitude, restaurant_AZ$latitude, col = km_AZ$cluster,
     pch = 20)
points(y = km_AZ$centers[,1], x = km_AZ$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_AZ <- (nrow(cbind(restaurant_AZ$latitude,restaurant_AZ$longitude)-1))*sum(apply(cbind(restaurant_AZ$latitude, restaurant_AZ$longitude,2,var)))
for (i in 1:20) { 
  wss_AZ[i] <- sum(kmeans(cbind(restaurant_AZ$latitude
                                            , restaurant_AZ$longitude),
                                     centers=i)$withinss)
}

plot(1:20, wss_AZ, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

######

km_NC <- kmeans(cbind(restaurant_NC$latitude, restaurant_NC$longitude), 
                centers = 11)
plot(restaurant_NC$longitude, restaurant_NC$latitude, col = km_NC$cluster,
     pch = 20)
points(y = km_NC$centers[,1], x = km_NC$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_NC <- (nrow(cbind(restaurant_NC$latitude,restaurant_NC$longitude)-1))*sum(apply(cbind(restaurant_NC$latitude, restaurant_NC$longitude,2,var)))
for (i in 1:20) { 
  wss_NC[i] <- sum(kmeans(cbind(restaurant_NC$latitude
                             , restaurant_NC$longitude),
                       centers=i)$withinss)
}

plot(1:20, wss_NC, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

###

km_NV <- kmeans(cbind(restaurant_NV$latitude, restaurant_NV$longitude), 
                centers = 15)
plot(restaurant_NV$longitude, restaurant_NV$latitude, col = km_NV$cluster,
     pch = 20)
points(y = km_NV$centers[,1], x = km_NV$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_NV <- (nrow(cbind(restaurant_NV$latitude,restaurant_NV$longitude)-1))*sum(apply(cbind(restaurant_NV$latitude, restaurant_NV$longitude,2,var)))
for (i in 1:20) { 
  wss_NV[i] <- sum(kmeans(cbind(restaurant_NV$latitude
                                , restaurant_NV$longitude),
                          centers=i)$withinss)
}

plot(1:20, wss_NV, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")


######

km_OH <- kmeans(cbind(restaurant_OH$latitude, restaurant_OH$longitude), 
                centers = 9)
plot(restaurant_OH$longitude, restaurant_OH$latitude, col = km_OH$cluster,
     pch = 20)
points(y = km_OH$centers[,1], x = km_OH$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_OH <- (nrow(cbind(restaurant_OH$latitude,restaurant_OH$longitude)-1))*sum(apply(cbind(restaurant_OH$latitude, restaurant_OH$longitude,2,var)))
for (i in 1:20) { 
  wss_OH[i] <- sum(kmeans(cbind(restaurant_OH$latitude
                                , restaurant_OH$longitude),
                          centers=i)$withinss)
}

plot(1:20, wss_OH, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")


####

km_PA <- kmeans(cbind(restaurant_PA$latitude, restaurant_PA$longitude), 
                centers = 12)
plot(restaurant_PA$longitude, restaurant_PA$latitude, col = km_PA$cluster,
     pch = 20)
points(y = km_PA$centers[,1], x = km_PA$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_PA <- (nrow(cbind(restaurant_PA$latitude,restaurant_PA$longitude)-1))*sum(apply(cbind(restaurant_PA$latitude, restaurant_PA$longitude,2,var)))
for (i in 1:20) { 
  wss_PA[i] <- sum(kmeans(cbind(restaurant_PA$latitude
                                , restaurant_PA$longitude),
                          centers=i)$withinss)
}

plot(1:20, wss_PA, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

####


km_WI <- kmeans(cbind(restaurant_WI$latitude, restaurant_WI$longitude), 
                centers = 8)
plot(restaurant_WI$longitude, restaurant_WI$latitude, col = km_WI$cluster,
     pch = 20)
points(y = km_WI$centers[,1], x = km_WI$centers[,2], col = "black",
       pch =13 , cex = 3)

wss_WI <- (nrow(cbind(restaurant_WI$latitude,restaurant_WI$longitude)-1))*sum(apply(cbind(restaurant_WI$latitude, restaurant_WI$longitude,2,var)))
for (i in 1:20) { 
  wss_WI[i] <- sum(kmeans(cbind(restaurant_WI$latitude
                                , restaurant_WI$longitude),
                          centers=i)$withinss)
}

plot(1:20, wss_WI, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")


write.table(km_AZ$centers, 
          col.names = F, row.names = F,
            file = 'clustering_centers_AZ.txt')

write.table(km_NC$centers, 
            col.names = F, row.names = F,
            file = 'clustering_centers_NC.txt')
write.table(km_NV$centers, 
            col.names = F, row.names = F,
            file = 'clustering_centers_NV.txt')
write.table(km_OH$centers, 
            col.names = F, row.names = F,
            file = 'clustering_centers_OH.txt')
write.table(km_PA$centers, 
            col.names = F, row.names = F,
            file = 'clustering_centers_PA.txt')
write.table(km_WI$centers, 
            col.names = F, row.names = F,
            file = 'clustering_centers_WI.txt')
