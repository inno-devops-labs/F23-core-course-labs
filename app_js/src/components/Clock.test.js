import React from 'react';
import {render, screen, waitFor} from '@testing-library/react';
import Clock from './Clock';

describe('Clock', () => {
    afterEach(() => {
        jest.clearAllMocks();
    });

    it('renders the city name', () => {
        render(<Clock city="Moscow" timezone="America/New_York"/>);
        expect(screen.getByText('Moscow')).toBeInTheDocument();
    });

    it('displays "Loading..." before loading the time', () => {
        render(<Clock city="New York" timezone="America/New_York"/>);
        expect(screen.getByText('Loading...')).toBeInTheDocument();
        expect(screen.queryByText(/(\d{2}:){2}\d{2}/)).toBeNull();
    });

    it('displays the formatted time after loading', async () => {
        render(<Clock city="New York" timezone="America/New_York"/>);
        await waitFor(() => {
            expect(screen.getByText(/\d{2}:\d{2}:\d{2}/)).toBeInTheDocument();
        });
        expect(screen.queryByText('Loading...')).toBeNull();
    });

});
