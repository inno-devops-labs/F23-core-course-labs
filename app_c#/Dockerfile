FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.18 AS build

COPY . /src

WORKDIR /src

RUN dotnet restore
RUN dotnet publish -c Release --no-restore -o /build

FROM mcr.microsoft.com/dotnet/aspnet:6.0-alpine3.18 AS runtime

COPY --from=build /build /app

RUN adduser -D limiteduser && chown -R limiteduser /app

USER limiteduser

WORKDIR /app

EXPOSE 80

ENTRYPOINT ["dotnet", "ProgrammerProfile.dll"]