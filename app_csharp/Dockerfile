FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 5001
EXPOSE 443

# Stage 1: Build and compile the app
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["app_csharp.csproj", "./"]
RUN dotnet restore "app_csharp.csproj"
COPY . .
WORKDIR "/src/"
RUN dotnet build "app_csharp.csproj" -c Release -o /app/build

# Stage 2: Publish the app
FROM build AS publish
RUN dotnet publish "app_csharp.csproj" -c Release -o /app/publish /p:UseAppHost=false

# Stage 3: Create final image
FROM base AS final
USER 1001
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "app_csharp.dll"]